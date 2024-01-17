"""Person CRUD"""


from app.database.base.crud import Crud
from app.models.person import PersonModel
from app.schemas.person import PersonCreateSchema, PersonUpdateSchema


class PersonCrud(Crud[PersonModel, PersonCreateSchema, PersonUpdateSchema]):
    """Person database methods"""
