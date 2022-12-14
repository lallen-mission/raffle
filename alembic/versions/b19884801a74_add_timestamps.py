"""add timestamps

Revision ID: b19884801a74
Revises: 5ecae21649f6
Create Date: 2022-09-15 09:05:26.867157

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b19884801a74'
down_revision = '5ecae21649f6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('drawingprizes', sa.Column('create_date', sa.DateTime(), nullable=True))
    op.add_column('drawings', sa.Column('create_date', sa.DateTime(), nullable=True))
    op.add_column('prizes', sa.Column('create_date', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('prizes', 'create_date')
    op.drop_column('drawings', 'create_date')
    op.drop_column('drawingprizes', 'create_date')
    # ### end Alembic commands ###