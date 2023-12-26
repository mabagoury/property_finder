"""rename table users to user

Revision ID: 011a2e7100fb
Revises: 488710ab0cb9
Create Date: 2023-12-23 09:51:30.537471

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '011a2e7100fb'
down_revision: Union[str, None] = '488710ab0cb9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.rename_table("users", "user")


def downgrade() -> None:
    op.rename_table("user", "user")
