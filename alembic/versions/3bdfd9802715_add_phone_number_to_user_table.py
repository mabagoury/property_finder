"""add phone_number to user table

Revision ID: 3bdfd9802715
Revises: 47bc15221436
Create Date: 2023-12-26 14:46:55.425566

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3bdfd9802715'
down_revision: Union[str, None] = '47bc15221436'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("users", sa.Column("phone_number", sa.Unicode(64)))


def downgrade() -> None:
    op.drop_column("user", "phone_number")
