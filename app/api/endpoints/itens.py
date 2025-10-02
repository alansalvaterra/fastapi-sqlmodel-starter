from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from typing import List

from app.core.database import get_session
from app.schemas.item import ItemCreate, ItemResponse, ItemUpdate
from app.crud.item import crud_item

router = APIRouter()

@router.post("/", response_model=ItemResponse)
def criar_item(item: ItemCreate, db: Session = Depends(get_session)):
    return crud_item.create(db, item)

@router.get("/", response_model=List[ItemResponse])
def listar_itens(skip: int = 0, limit: int = 100, db: Session = Depends(get_session)):
    return crud_item.get_all(db, skip=skip, limit=limit)

@router.get("/{id}", response_model=ItemResponse)
def buscar_item(id: int, db: Session = Depends(get_session)):
    item = crud_item.get(db, id)
    if not item:
        raise HTTPException(status_code=404, detail="Item não encontrado")
    return item

@router.put("/{id}", response_model=ItemResponse)
def atualizar_item(
    id: int, 
    item: ItemUpdate, 
    db: Session = Depends(get_session)
):
    """Atualiza um item existente"""
    db_item = crud_item.get(db, id)
    if not db_item:
        raise HTTPException(status_code=404, detail="Item não encontrado")
    
    return crud_item.update(db, db_item, item)

@router.patch("/{id}", response_model=ItemResponse)
def atualizar_item_parcial(
    id: int, 
    item: ItemUpdate, 
    db: Session = Depends(get_session)
):
    """Atualiza parcialmente um item existente"""
    db_item = crud_item.get(db, id)
    if not db_item:
        raise HTTPException(status_code=404, detail="Item não encontrado")
    
    return crud_item.update(db, db_item, item)

@router.delete("/{id}")
def deletar_item(id: int, db: Session = Depends(get_session)):
    """Deleta um item"""
    db_item = crud_item.get(db, id)
    if not db_item:
        raise HTTPException(status_code=404, detail="Item não encontrado")
    
    crud_item.delete(db, id)
    return {"message": "Item deletado com sucesso"}