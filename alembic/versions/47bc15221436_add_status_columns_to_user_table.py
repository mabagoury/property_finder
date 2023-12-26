"""add status columns to user table

Revision ID: 47bc15221436
Revises: 011a2e7100fb
Create Date: 2023-12-25 07:21:17.805344

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '47bc15221436'
down_revision: Union[str, None] = '011a2e7100fb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("user", sa.Column("is_active", sa.Boolean()))
    op.add_column("user", sa.Column("is_superuser", sa.Boolean))
    op.add_column("user", sa.Column("is_verified", sa.Boolean()))


def downgrade() -> None:
    op.drop_column("user", "is_verified")
    op.drop_column("user", "is_superuser")
    op.drop_column("user", "is_active")
