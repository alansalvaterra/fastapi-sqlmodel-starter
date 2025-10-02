from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class Item(SQLModel, table=True):
    """Modelo genérico para demonstração"""
    
    id: Optional[int] = Field(default=None, primary_key=True)
    nome: str = Field(index=True, max_length=100)
    descricao: Optional[str] = Field(default=None, max_length=500)
    preco: Optional[float] = Field(default=None)
    quantidade: int = Field(default=1)
    ativo: bool = Field(default=True)
    criado_em: datetime = Field(default_factory=datetime.utcnow)
    