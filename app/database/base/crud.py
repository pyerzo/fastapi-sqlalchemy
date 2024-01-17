"""CRUD base operations"""

from typing import Any, Generic, Type, TypeVar

from sqlalchemy import delete, insert, select, update
from sqlalchemy.orm import Session

ModelType = TypeVar("ModelType")
CreateSchema = TypeVar("CreateSchema")
UpdateSchema = TypeVar("UpdateSchema")


class Crud(Generic[ModelType, CreateSchema, UpdateSchema]):
    """Class for generic database methods"""

    def __init__(self, session: Session, model: Type[ModelType]):
        self.session = session
        self.model = model

    def get(self, record_id: Any):
        """Get one record by id"""
        model_id: Any = self.model.id  # type: ignore
        return self.session.scalars(
            select(self.model).where(model_id == record_id)
        ).one_or_none()

    def get_all(self):
        """Get all recors from table"""
        return self.session.scalars(select(self.model)).all()

    def create(self, data: CreateSchema):
        """Create one record"""
        _data: Any = data.dict()  # type: ignore
        return self.session.execute(insert(self.model), _data)

    def update(self, record_id: Any, data: UpdateSchema):
        """Update one record"""
        _data: Any = data.dict(exclude_unset=True)  # type: ignore
        model_id: Any = self.model.id  # type: ignore
        return self.session.execute(
            update(self.model).where(model_id == record_id), _data
        )

    def delete(self, record_id: Any):
        """Delete one record"""
        model_id: Any = self.model.id  # type: ignore
        return self.session.execute(
            delete(self.model).where(model_id == record_id),
        )
