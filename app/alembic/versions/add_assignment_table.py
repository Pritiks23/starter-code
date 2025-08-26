"""add assignment table

Revision ID: add_assignment_table
Revises: 
Create Date: 2025-08-26 00:00:00.000000

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'add_assignment_table'
down_revision = "2dcfc2ce13cb"
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        'assignment',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('title', sa.String(length=255), nullable=False),
        sa.Column('body', sa.Text, nullable=False),
        sa.Column('submission_date', sa.DateTime, nullable=False),
        sa.Column('classroom_id', sa.Integer, sa.ForeignKey('classroom.id', ondelete='CASCADE'), nullable=False),
        sa.Column('student_id', sa.Integer, sa.ForeignKey('user_account.id', ondelete='CASCADE'), nullable=False),
    )

def downgrade():
    op.drop_table('assignment')
