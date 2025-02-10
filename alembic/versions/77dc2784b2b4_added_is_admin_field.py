"""Added is_admin field

Revision ID: 77dc2784b2b4
Revises: 39c04ac1b96b
Create Date: 2025-02-10 13:11:13.377089

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '77dc2784b2b4'
down_revision: Union[str, None] = '39c04ac1b96b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
