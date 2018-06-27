"""followers

Revision ID: 03102364f39f
Revises: a89a7f5c29de
Create Date: 2018-06-27 14:55:39.668912

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '03102364f39f'
down_revision = 'a89a7f5c29de'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###
