"""Person schemas"""

from datetime import date
from typing import Optional
from pydantic import BaseModel


class Base(BaseModel):
    """Base schema"""

    birth_date: Optional[date] = None


class PersonSchema(Base):
    """Person object schema"""

    id: str
    name: str
    active: bool


class PersonCreateSchema(Base):
    """Person data create schema"""

    name: str


class PersonUpdateSchema(Base):
    """Person data update schema"""

    name: Optional[str] = None
    active: Optional[bool] = None
