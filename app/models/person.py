"""Person database model"""

from datetime import date
from typing import Optional
from uuid import UUID

from sqlalchemy import Uuid, text
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base.session import Base


class PersonModel(Base):
    """Defines model for Person"""

    __tablename__ = "person"

    id: Mapped[UUID] = mapped_column(
        Uuid,
        primary_key=True,
        server_default=text("gen_random_uuid()"),
    )
    name: Mapped[str]
    birth_date: Mapped[Optional[date]]
    active: Mapped[bool] = mapped_column(default=True)
