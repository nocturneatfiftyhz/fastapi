"""add content column to posts table

Revision ID: 5d49aa18d492
Revises: 1e004da471c1
Create Date: 2023-02-05 00:30:32.510528

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5d49aa18d492'
down_revision = '1e004da471c1'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
