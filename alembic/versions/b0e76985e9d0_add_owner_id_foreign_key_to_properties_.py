"""add owner_id foreign key to properties table

Revision ID: b0e76985e9d0
Revises: ea7ec60c0b89
Create Date: 2023-12-23 06:44:20.479886

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b0e76985e9d0'
down_revision: Union[str, None] = 'ea7ec60c0b89'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column("properties", sa.Column("owner_id", sa.Integer))

    op.create_foreign_key(
        'fk_owner_id',
        'properties', 'users',
        ['owner_id'], ['id'],
    )


def downgrade():
    op.drop_constraint('owner_id', 'properties')

    op.drop_column("properties", "owner_id")
