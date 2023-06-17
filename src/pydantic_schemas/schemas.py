from pydantic import BaseModel, UUID4


class Key(BaseModel):
    key: str


class PetSolo(BaseModel):
    age: str
    animal_type: str
    created_at: str
    id: UUID4
    name: str
    pet_photo: str
    user_id: str


class PetInList(BaseModel):
    age: str
    animal_type: str
    created_at: str
    id: str
    name: str
    pet_photo: str


