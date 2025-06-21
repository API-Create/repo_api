from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base

class Color(Base):
    __tablename__ = "colors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    image = Column(String(255), nullable=False)
    semibot_id = Column(Integer, ForeignKey("semibots.id"))

    semibot = relationship("Semibot", back_populates="colors")
