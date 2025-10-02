from sqlmodel import SQLModel, create_engine, Session
from .config import settings

# Engine para PostgreSQL
engine = create_engine(
    settings.DATABASE_URL,
    echo=True,  # Mostra SQL no console
    # PostgreSQL não precisa do check_same_thread
    pool_size=10,  # Conexões simultâneas
    max_overflow=20  # Conexões extras temporárias
)

def create_db_and_tables():
    """Cria todas as tabelas no banco de dados PostgreSQL"""
    SQLModel.metadata.create_all(engine)

def get_session():
    """Fornece sessão de banco de dados para operações"""
    with Session(engine) as session:
        yield session