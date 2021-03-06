"""empty message

Revision ID: 53a86055ebb9
Revises: 
Create Date: 2020-07-23 20:36:24.097669

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '53a86055ebb9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('id', sa.Integer(), nullable=False))
    op.alter_column('user', 'email',
               existing_type=mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=120),
               nullable=True)
    op.drop_index('ix_user_email', table_name='user')
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.create_index('ix_user_email', 'user', ['email'], unique=False)
    op.alter_column('user', 'email',
               existing_type=mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=120),
               nullable=False)
    op.drop_column('user', 'id')
    # ### end Alembic commands ###
