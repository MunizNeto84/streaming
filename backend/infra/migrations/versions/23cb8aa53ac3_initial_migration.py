"""initial migration

Revision ID: 23cb8aa53ac3
Revises: 
Create Date: 2024-07-18 13:18:00.229236

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '23cb8aa53ac3'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'videos',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('titulo', sa.String(255), nullable=False),
        sa.Column('descricao', sa.String(255), nullable=False),
        sa.Column('url', sa.String(255), nullable=False),
    )


def downgrade() -> None:
    op.drop_table('videos')
