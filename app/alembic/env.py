"""add assignment table

Revision ID: add_assignment_table
Revises: 
Create Date: 2025-08-26 09:00:00.000000

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'add_assignment_table'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    # Create assignment table
    op.create_table(
        'assignment',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True, index=True),
        sa.Column('title', sa.String(length=255), nullable=False),
        sa.Column('body', sa.String, nullable=True),
        sa.Column('submission_date', sa.DateTime, nullable=True),
        sa.Column('classroom_id', sa.Integer, sa.ForeignKey('classroom.id', ondelete='CASCADE'), nullable=False),
        sa.Column('student_id', sa.Integer, sa.ForeignKey('user_account.id', ondelete='CASCADE'), nullable=False),
    )

def downgrade():
    # Drop assignment table
    op.drop_table('assignment')

