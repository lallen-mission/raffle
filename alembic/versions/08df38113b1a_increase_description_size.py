"""increase description size

Revision ID: 08df38113b1a
Revises: 5452cc4a22e4
Create Date: 2022-09-14 14:42:08.345945

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '08df38113b1a'
down_revision = '5452cc4a22e4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'drawingprizes', ['id'])
    op.create_unique_constraint(None, 'drawings', ['id'])
    op.create_unique_constraint(None, 'entries', ['id'])
    op.create_unique_constraint(None, 'prizes', ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'prizes', type_='unique')
    op.drop_constraint(None, 'entries', type_='unique')
    op.drop_constraint(None, 'drawings', type_='unique')
    op.drop_constraint(None, 'drawingprizes', type_='unique')
    # ### end Alembic commands ###