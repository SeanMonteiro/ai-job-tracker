"""add job status

Revision ID: 06c0ad10dbf7
Revises: 0bc518755d0e
Create Date: 2026-05-16 21:49:08.167168

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '06c0ad10dbf7'
down_revision: Union[str, Sequence[str], None] = '0bc518755d0e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column(
        "jobs",
        sa.Column(
            "status",
            sa.String(length=50),
            nullable="False",
            server_default = sa.text("'Saved'")
        )
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column("jobs","status")
