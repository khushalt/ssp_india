"""empty message

Revision ID: 4c98fb71f156
Revises: 53a86055ebb9
Create Date: 2020-07-23 20:38:10.117501

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '4c98fb71f156'
down_revision = '53a86055ebb9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'full_name',
               existing_type=mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=180),
               nullable=False)
    op.alter_column('user', 'password_hash',
               existing_type=mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=128),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'password_hash',
               existing_type=mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=128),
               nullable=True)
    op.alter_column('user', 'full_name',
               existing_type=mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=180),
               nullable=True)
    # ### end Alembic commands ###
