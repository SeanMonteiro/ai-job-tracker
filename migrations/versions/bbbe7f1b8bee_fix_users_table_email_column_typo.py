"""fix users table email column typo

Revision ID: bbbe7f1b8bee
Revises: 374d3326c5ad
Create Date: 2026-05-07 20:39:36.760211

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bbbe7f1b8bee'
down_revision: Union[str, Sequence[str], None] = '374d3326c5ad'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.alter_column("users", "emal", new_column_name="email")


def downgrade() -> None:
    """Downgrade schema."""
    pass
