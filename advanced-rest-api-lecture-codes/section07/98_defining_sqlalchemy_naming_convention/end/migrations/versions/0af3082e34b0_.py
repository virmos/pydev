"""empty message

Revision ID: 0af3082e34b0
Revises: 3a9f65801ff9
Create Date: 2018-10-25 17:37:15.876967

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0af3082e34b0'
down_revision = '3a9f65801ff9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('email', sa.String(length=80), nullable=False))
    op.create_unique_constraint(op.f('uq_users_email'), 'users', ['email'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(op.f('uq_users_email'), 'users', type_='unique')
    op.drop_column('users', 'email')
    # ### end Alembic commands ###
