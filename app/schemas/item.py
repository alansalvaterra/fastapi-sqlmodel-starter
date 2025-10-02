from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ItemCreate(BaseModel):
    nome: str
    descricao: Optional[str] = None
    preco: Optional[float] = None
    quantidade: int = 1

class ItemUpdate(BaseModel):
    nome: Optional[str] = None
    descricao: Optional[str] = None
    preco: Optional[float] = None
    quantidade: Optional[int] = None
    ativo: Optional[bool] = None

class ItemResponse(BaseModel):
    id: int
    nome: str
    descricao: Optional[str]
    preco: Optional[float]
    quantidade: int
    ativo: bool
    criado_em: datetime
    
    class Config:
        from_attributes = True