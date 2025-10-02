import sys
import os
from datetime import datetime

# Adiciona o diretório raiz ao path do Python
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sqlmodel import create_engine, Session, select
from app.core.config import settings
from app.models.item import Item 

def seed_database():
    """Popula o banco com dados de teste"""
    engine = create_engine(settings.DATABASE_URL)
    
    with Session(engine) as session:
        # Verifica se já existem dados
        statement = select(Item)
        existing = session.exec(statement).first()
        if existing:
            print("✅ Banco já possui dados. Skip seed.")
            return
        
        # Dados de exemplo GENÉRICOS
        itens = [
            Item(
                nome="Notebook Dell", 
                descricao="Notebook i7, 16GB RAM", 
                preco=2500.00, 
                quantidade=5
            ),
            Item(
                nome="Mouse Wireless", 
                descricao="Mouse ergonômico sem fio", 
                preco=89.90, 
                quantidade=20
            ),
            Item(
                nome="Teclado Mecânico", 
                descricao="Teclado RGB switches blue", 
                preco=299.00, 
                quantidade=8
            ),
            Item(
                nome='Monitor 24"', 
                descricao="Monitor Full HD IPS", 
                preco=799.00, 
                quantidade=3
            ),
            Item(
                nome="Webcam HD", 
                descricao="Webcam 1080p com microfone", 
                preco=159.90, 
                quantidade=15
            ),
        ]
        
        session.add_all(itens)
        session.commit()
        print(f"✅ {len(itens)} itens inseridos com sucesso!")

if __name__ == "__main__":
    seed_database()