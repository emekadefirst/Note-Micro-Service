from src.utilities.repository import NoteBaseRepository
from src.core.models import Note
from fastapi import HTTPException
from src.core.schemas import NoteSchema, NoteSchemaObject


class NoteService:
    boa = NoteBaseRepository(Note)

    @classmethod
    async def create(cls, dto: NoteSchema):
        return await cls.boa.model.create(**dto.dict())
    
    @classmethod
    async def list(cls):
        return await cls.boa.all()
    
    @classmethod
    async def get(cls, id: str):
        return await cls.boa.get_obj(id=id)

    @classmethod 
    async def delete(cls, id: str):
        return await cls.boa.trash(id=id)
    
    @classmethod
    async def update(cls, id: str, dto: NoteSchema):
        obj = await cls.boa.get_obj(id=id)
        if not obj:
            raise HTTPException(status_code=404, detail="Note not found")

        update_data = dto.dict(exclude_unset=True, exclude_none=True)
        for field, value in update_data.items():
            setattr(obj, field, value)
        return await obj.save()
    