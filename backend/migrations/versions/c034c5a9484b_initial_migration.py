"""Initial migration

Revision ID: c034c5a9484b
Revises: 
Create Date: 2021-06-02 00:51:52.044591

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c034c5a9484b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('chapter', 'course_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.add_column('course', sa.Column('course_image', sa.String(length=100), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('course', 'course_image')
    op.alter_column('chapter', 'course_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###