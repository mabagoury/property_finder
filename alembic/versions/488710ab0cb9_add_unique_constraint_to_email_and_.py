"""add unique constraint to email and username columns in users table

Revision ID: 488710ab0cb9
Revises: 26582e890990
Create Date: 2023-12-23 07:52:05.137473

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '488710ab0cb9'
down_revision: Union[str, None] = '26582e890990'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_unique_constraint("uq_email", "users", ["email"])

    op.create_unique_constraint("uq_username", "users", ["username"])


def downgrade() -> None:
    op.drop_constraint("uq_email", "users")
    # op.drop_index("ik_email", "users")

    op.drop_constraint("uq_username", "users")
    # op.drop_index("ik_username", "users")
