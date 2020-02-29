"""add token for user

Revision ID: f1dca56dfb7d
Revises: 4fd934c98db8
Create Date: 2020-02-29 11:53:10.263135

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f1dca56dfb7d'
down_revision = '4fd934c98db8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('token', sa.String(length=180), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'token')
    # ### end Alembic commands ###