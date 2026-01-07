from app.db_config import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, ForeignKey, String

class Questao(Base):
    __tablename__ = "questao"

    titulo: Mapped[str] = mapped_column(String(50), nullable=False)
    quantidade_respostas: Mapped[int] = mapped_column(Integer, nullable=True, default=0)
    pergunta_id: Mapped[int] = mapped_column(
        ForeignKey("pergunta.id", ondelete="CASCADE"),
        nullable=False
    )

    pergunta: Mapped["Pergunta"] = relationship(
        back_populates="questoes"
    )

    def __init__(self, pergunta_id: int, titulo: str, quantidade_respostas: int = 0):
        
        self.pergunta_id = pergunta_id
        self.titulo = titulo
        self.quantidade_respostas = quantidade_respostas