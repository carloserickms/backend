
from app.db_config import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Boolean, Integer, String
from typing import List

class Formulario(Base):
    __tablename__ = "formulario"

    titulo: Mapped[str] = mapped_column(String(50), nullable=False)
    ativo: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)

    perguntas: Mapped[List["Pergunta"]] = relationship(
        back_populates="formulario",
        cascade="all, delete-orphan"
    )

    def __init__(self, titulo: str, ativo: bool = True):
        self.titulo = titulo
        self.ativo = ativo
