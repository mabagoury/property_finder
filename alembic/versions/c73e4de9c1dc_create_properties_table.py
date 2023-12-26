"""create properties table

Revision ID: c73e4de9c1dc
Revises: 
Create Date: 2023-12-22 03:04:22.825705

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c73e4de9c1dc'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'properties',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('title', sa.String(50), nullable=False),
        sa.Column('address', sa.Unicode(200)),
        sa.Column('description', sa.Unicode(400)),
    )


def downgrade() -> None:
    op.drop_table('properties')
