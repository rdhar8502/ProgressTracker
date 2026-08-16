"""add_category_to_dsa_problems

Revision ID: a8d712f3b49e
Revises: 6f31de6a10f9
Create Date: 2026-08-16 08:40:00.000000

"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a8d712f3b49e'
down_revision: Union[str, None] = '6f31de6a10f9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('dsa_problems', sa.Column('category', sa.String(length=100), nullable=True, server_default='Arrays and Strings'))
    # Set default and infer from topic if available
    op.execute("""
        UPDATE dsa_problems
        SET category = (
            SELECT t.name
            FROM dsa_problem_topics pt
            JOIN dsa_topics t ON pt.topic_id = t.id
            WHERE pt.problem_id = dsa_problems.id
            LIMIT 1
        )
        WHERE category IS NULL OR category = '';
    """)
    op.execute("UPDATE dsa_problems SET category = 'Arrays and Strings' WHERE category IS NULL OR category = '';")


def downgrade() -> None:
    op.drop_column('dsa_problems', 'category')
