"""empty message

Revision ID: 6c7f91149ce1
Revises: 
Create Date: 2019-05-28 23:36:29.296134

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6c7f91149ce1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('document',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=256), nullable=True),
    sa.Column('category', sa.String(length=128), nullable=True),
    sa.Column('user', sa.String(length=128), nullable=True),
    sa.Column('avaliado', sa.Boolean(), nullable=True),
    sa.Column('directory', sa.String(length=128), nullable=True),
    sa.Column('time', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('permission',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=128), nullable=True),
    sa.Column('level', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('permission')
    op.drop_table('document')
    # ### end Alembic commands ###
