from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.models import semibot as semibot_model
from app.schemas import semibot as semibot_schema
from app.core.config import settings

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Función utilitaria para agregar la URL completa a las imágenes
def set_image_urls(colors):
    for c in colors:
        c.image = f"{settings.BASE_URL}/static/semibots/{c.image}"
    return colors


@router.get("/semibot", response_model=semibot_schema.SemibotOut)
def get_main_semibot(db: Session = Depends(get_db)):
    semibot = db.query(semibot_model.Semibot).first()
    if not semibot:
        raise HTTPException(status_code=404, detail="Semibot no encontrado")

    semibot.colors = set_image_urls(semibot.colors)
    return semibot


@router.get("/semibot/colors/{color_name}", response_model=semibot_schema.SemibotOut)
def get_semibot_by_color(color_name: str, db: Session = Depends(get_db)):
    if not color_name.strip():
        raise HTTPException(status_code=400, detail="Nombre de color inválido")

    semibot = db.query(semibot_model.Semibot).first()
    if not semibot:
        raise HTTPException(status_code=404, detail="Semibot no encontrado")

    filter_colors = [c for c in semibot.colors if c.name.lower() == color_name.lower()]
    if not filter_colors:
        raise HTTPException(status_code=404, detail=f"Color '{color_name}' no encontrado")

    semibot.colors = set_image_urls(filter_colors)
    return semibot
