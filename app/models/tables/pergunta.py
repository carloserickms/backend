from app.db_config import Base
from typing import List
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, ForeignKey, String


class Pergunta(Base):
    __tablename__ = "pergunta"


    titulo: Mapped[str] = mapped_column(String(50), nullable=False)
    formulario_id: Mapped[int] = mapped_column(
        ForeignKey("formulario.id", ondelete="CASCADE"),
        nullable=False
    )

    questoes: Mapped[List["Questao"]] = relationship(
        back_populates="pergunta",
        cascade="all, delete-orphan"
    )

    formulario: Mapped["Formulario"] = relationship(
        back_populates="perguntas"
    )    

    def __init__(self, formulario_id: int, titulo: str):

        self.formulario_id = formulario_id
        self.titulo = titulo