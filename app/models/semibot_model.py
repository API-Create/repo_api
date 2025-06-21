from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from app.db.database import Base

class Semibot(Base):
    __tablename__ = "semibots"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    image = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)

    colors = relationship("Color", back_populates="semibot", cascade="all, delete-orphan")
