from sqlmodel import Session, select
from typing import List, Optional
from app.models.item import Item
from app.schemas.item import ItemCreate, ItemUpdate

class CRUDItem:
    def create(self, db: Session, item: ItemCreate) -> Item:
        db_item = Item(**item.dict())
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item
    
    def get(self, db: Session, id: int) -> Optional[Item]:
        return db.exec(select(Item).where(Item.id == id)).first()
    
    def get_all(self, db: Session, skip: int = 0, limit: int = 100) -> List[Item]:
        return db.exec(select(Item).offset(skip).limit(limit)).all()
    
    def get_by_nome(self, db: Session, nome: str) -> List[Item]:
        return db.exec(select(Item).where(Item.nome == nome)).all()
    
    def update(self, db: Session, db_item: Item, item_update: ItemUpdate) -> Item:
        """Atualiza um item existente"""
        update_data = item_update.dict(exclude_unset=True)
        
        for field, value in update_data.items():
            setattr(db_item, field, value)
            
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item
    
    def delete(self, db: Session, id: int) -> None:
        """Deleta um item"""
        db_item = self.get(db, id)
        if db_item:
            db.delete(db_item)
            db.commit()

crud_item = CRUDItem()