"""Add 'readonly' resource lock type to db ontology

Revision ID: 10f9e72e72aa
Revises: 5b80d059cbb4
Create Date: 2024-06-28 10:12:34.014151

"""

from typing import Annotated

import sqlalchemy as sa
from alembic import op
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    MappedAsDataclass,
    mapped_column,
    sessionmaker,
)

# revision identifiers, used by Alembic.
revision = "10f9e72e72aa"
down_revision = "5b80d059cbb4"
branch_labels = None
depends_on = None


# Migration data models
text_ = Annotated[str, mapped_column(sa.Text())]


class UpgradeBase(DeclarativeBase, MappedAsDataclass):
    pass


class ResourceLockTypeUpgrade(UpgradeBase):
    __tablename__ = "resource_lock_types"

    resource_lock_type: Mapped[text_] = mapped_column(primary_key=True)


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    bind = op.get_bind()
    Session = sessionmaker(bind=bind)

    with Session() as session:
        # Check whether the readonly lock type is already in the database definition
        # (this can happen if you upgrade then downgrade this migration).
        readonly_lock_type_stmt = sa.select(ResourceLockTypeUpgrade).where(
            ResourceLockTypeUpgrade.resource_lock_type == "readonly"
        )

        if session.scalar(readonly_lock_type_stmt) is None:
            # Add "readonly" to lock types table if its missing.
            session.add(ResourceLockTypeUpgrade(resource_lock_type="readonly"))

        session.commit()


def downgrade():
    # No downgrade necessary, the readonly entry in the resource_lock_types table
    # doesn't affect any other functionality.
    pass