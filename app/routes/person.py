"""Person router"""

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database.base.session import get_session
from app.database.person import PersonCrud
from app.models.person import PersonModel
from app.schemas.person import PersonCreateSchema, PersonUpdateSchema

router = APIRouter(prefix="/person", tags=["Person"])


@router.get(path="/", status_code=status.HTTP_200_OK)
async def get_person(database: Session = Depends(get_session)):
    """Search a person by id"""
    person_crud = PersonCrud(database, PersonModel)
    return person_crud.get_all()


@router.post(path="/", status_code=status.HTTP_200_OK)
async def save_person(
    data: PersonCreateSchema,
    database: Session = Depends(get_session),
):
    """Create a person record"""
    person_crud = PersonCrud(database, PersonModel)
    person_crud.create(data)
    database.commit()


@router.put(path="/{id}", status_code=status.HTTP_200_OK)
async def update_person(
    data: PersonUpdateSchema,
    record_id: str,
    database: Session = Depends(get_session),
):
    """Update a person record"""
    person_crud = PersonCrud(database, PersonModel)
    person_crud.update(record_id, data)
    database.commit()


@router.delete(path="/{record_id}", status_code=status.HTTP_200_OK)
async def remove_person(
    record_id: str,
    database: Session = Depends(get_session),
):
    """Remove a person record"""
    person_crud = PersonCrud(database, PersonModel)
    person_crud.delete(record_id)
    database.commit()
