"""add cascading deletion

Revision ID: a9079d829436
Revises: b19884801a74
Create Date: 2022-09-15 09:08:53.486345

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a9079d829436'
down_revision = 'b19884801a74'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('drawingprizes_prize_id_fkey', 'drawingprizes', type_='foreignkey')
    op.drop_constraint('drawingprizes_winner_fkey', 'drawingprizes', type_='foreignkey')
    op.create_foreign_key(None, 'drawingprizes', 'prizes', ['prize_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key(None, 'drawingprizes', 'entries', ['winner'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'drawingprizes', type_='foreignkey')
    op.drop_constraint(None, 'drawingprizes', type_='foreignkey')
    op.create_foreign_key('drawingprizes_winner_fkey', 'drawingprizes', 'entries', ['winner'], ['id'])
    op.create_foreign_key('drawingprizes_prize_id_fkey', 'drawingprizes', 'prizes', ['prize_id'], ['id'])
    # ### end Alembic commands ###