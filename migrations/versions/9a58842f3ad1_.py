"""empty message

Revision ID: 9a58842f3ad1
Revises: 4c98fb71f156
Create Date: 2020-07-23 21:47:26.352596

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '9a58842f3ad1'
down_revision = '4c98fb71f156'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'password_hash',
               existing_type=mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=128),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'password_hash',
               existing_type=mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=128),
               nullable=False)
    # ### end Alembic commands ###
