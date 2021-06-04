"""empty message

Revision ID: 3e3b5458caf1
Revises: 2ce406d0c865
Create Date: 2021-06-04 12:27:42.049551

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3e3b5458caf1'
down_revision = '2ce406d0c865'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comment', sa.Column('date', sa.DateTime(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('comment', 'date')
    # ### end Alembic commands ###
