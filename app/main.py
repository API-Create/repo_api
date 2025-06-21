from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.api import semibots
from app.db.database import Base, engine

# Crear tablas
Base.metadata.create_all(bind=engine)

app = FastAPI(title="REPO API - Semibot")

# Montar carpeta de imágenes
app.mount("/semibot", StaticFiles(directory="static/semibots"), name="semibots")

app.include_router(semibots.router)
