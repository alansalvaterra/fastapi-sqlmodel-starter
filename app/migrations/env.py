from logging.config import fileConfig
from sqlmodel import SQLModel
from alembic import context
import os
import sys

# Adiciona o diretório app ao path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

# Importa as configurações do projeto
from app.core.config import settings

# Importa todos os modelos para o Alembic reconhecer as tabelas
from app.models.item import Item 
# Adicione outros modelos conforme necessário

# Configuração do Alembic
config = context.config

# Configura logger se arquivo de config existe
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Metadata para migrations
target_metadata = SQLModel.metadata

def run_migrations_offline():
    """Run migrations in 'offline' mode."""
    url = settings.DATABASE_URL
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    """Run migrations in 'online' mode."""
    from sqlmodel import create_engine
    
    # Usa a URL do nosso settings
    connectable = create_engine(settings.DATABASE_URL)

    with connectable.connect() as connection:
        context.configure(
            connection=connection, 
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()