"""add user table

Revision ID: 33c2150ae60e
Revises: 5d49aa18d492
Create Date: 2023-02-05 00:37:19.641305

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '33c2150ae60e'
down_revision = '5d49aa18d492'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('id')
                    )
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
