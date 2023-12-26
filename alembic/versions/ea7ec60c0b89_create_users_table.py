"""create users table

Revision ID: ea7ec60c0b89
Revises: c73e4de9c1dc
Create Date: 2023-12-23 06:44:07.477788

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ea7ec60c0b89'
down_revision: Union[str, None] = 'c73e4de9c1dc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('username', sa.Unicode(50), nullable=False),
        sa.Column('email', sa.Unicode(50), nullable=False),
        sa.Column('age', sa.Integer),
    )


def downgrade() -> None:
    op.drop_table('users')
