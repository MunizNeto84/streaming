"""add categoria table and update videos table

Revision ID: f07ecc6a8fda
Revises: 23cb8aa53ac3
Create Date: 2024-07-20 14:21:26.354785

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f07ecc6a8fda'
down_revision: Union[str, None] = '23cb8aa53ac3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'categoria',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('titulo', sa.String(255), nullable=False),
        sa.Column('cor', sa.String(255), nullable=False),
    )
    
    op.add_column('videos', sa.Column('categoria_id', sa.Integer, sa.ForeignKey('categoria.id')))



def downgrade() -> None:
    op.drop_column('videos', 'categoria_id')
    op.drop_table('categoria')
