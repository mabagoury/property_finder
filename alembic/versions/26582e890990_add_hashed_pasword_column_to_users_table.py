"""add hashed_pasword column to users table

Revision ID: 26582e890990
Revises: b0e76985e9d0
Create Date: 2023-12-23 07:37:12.675690

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '26582e890990'
down_revision: Union[str, None] = 'b0e76985e9d0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("users", sa.Column("hashed_password", sa.String))


def downgrade() -> None:
    op.drop_column("users", "hashed_password")
