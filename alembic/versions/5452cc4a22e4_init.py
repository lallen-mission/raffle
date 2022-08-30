"""init

Revision ID: 5452cc4a22e4
Revises: 
Create Date: 2022-08-30 15:05:29.440444

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5452cc4a22e4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('drawings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('date_started', sa.DateTime(), nullable=True),
    sa.Column('date_ended', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('prizes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=150), nullable=True),
    sa.Column('image_url', sa.String(length=300), nullable=True),
    sa.Column('description', sa.String(length=300), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.String(length=50), nullable=False),
    sa.Column('register_date', sa.DateTime(), nullable=True),
    sa.Column('last_login_date', sa.DateTime(), nullable=True),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.Column('profile_pic', sa.String(length=150), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('entries',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('uuid', sa.String(length=100), nullable=True),
    sa.Column('create_date', sa.DateTime(), nullable=True),
    sa.Column('created_by', sa.String(length=50), nullable=True),
    sa.Column('confirmed', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['created_by'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id'),
    sa.UniqueConstraint('uuid')
    )
    op.create_table('drawingprizes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('prize_id', sa.Integer(), nullable=True),
    sa.Column('drawing_id', sa.Integer(), nullable=True),
    sa.Column('winner', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['drawing_id'], ['drawings.id'], ),
    sa.ForeignKeyConstraint(['prize_id'], ['prizes.id'], ),
    sa.ForeignKeyConstraint(['winner'], ['entries.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('drawingprizes')
    op.drop_table('entries')
    op.drop_table('users')
    op.drop_table('prizes')
    op.drop_table('drawings')
    # ### end Alembic commands ###