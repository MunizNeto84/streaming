"""add dados inicias na tabela categoria

Revision ID: b910fb8ad713
Revises: f07ecc6a8fda
Create Date: 2024-07-21 12:13:37.974608

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b910fb8ad713'
down_revision: Union[str, None] = 'f07ecc6a8fda'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(
        "INSERT INTO categoria (id, titulo, cor) VALUES (1, 'Livre', 'cinza')"
    )


def downgrade() -> None:
    op.drop_column('videos', 'categoria_id')
    op.drop_table('categoria')
