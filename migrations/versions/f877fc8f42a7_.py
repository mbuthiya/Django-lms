"""empty message

Revision ID: f877fc8f42a7
Revises: f4893051b14d
Create Date: 2017-09-14 17:21:08.754021

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f877fc8f42a7'
down_revision = 'f4893051b14d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('lessons', 'lesson_day')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('lessons', sa.Column('lesson_day', sa.VARCHAR(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
