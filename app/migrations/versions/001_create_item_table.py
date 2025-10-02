"""Create items table

Revision ID: 001
Revises: 
Create Date: 2025-01-01 10:00:00.000000

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '001'
down_revision = None
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.create_table('item',  # ← MUDE para SINGULAR
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=100), nullable=False),
    sa.Column('descricao', sa.String(length=500), nullable=True),
    sa.Column('preco', sa.Float(), nullable=True),
    sa.Column('quantidade', sa.Integer(), nullable=False),
    sa.Column('ativo', sa.Boolean(), nullable=False),
    sa.Column('criado_em', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_item_nome'), 'item', ['nome'], unique=False)  # ← SINGULAR

def downgrade() -> None:
    op.drop_index(op.f('ix_item_nome'), table_name='item')  # ← SINGULAR
    op.drop_table('item')  # ← SINGULAR