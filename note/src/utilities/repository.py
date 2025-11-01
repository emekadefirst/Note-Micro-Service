from typing import Type, List, Optional
from tortoise import Model
from tortoise.exceptions import DoesNotExist


class NoteBaseRepository:
    def __init__(self, model: Type[Model]):
        self.model = model

    async def all(self, prefetch_related: Optional[List[str]] = None):
        query = self.model.all().order_by('-created_at', '-updated_at')

        if hasattr(self.model, "is_deleted"):
            query = query.filter(is_deleted=False)

        if prefetch_related:
            query = query.prefetch_related(*prefetch_related)

        return await query

    async def filter(self, prefetch_related: Optional[List[str]] = None, **kwargs):
        query = self.model.filter(**kwargs).order_by('-created_at', '-updated_at')

        if hasattr(self.model, "is_deleted"):
            query = query.filter(is_deleted=False)

        if prefetch_related:
            query = query.prefetch_related(*prefetch_related)

        return await query

    async def get_obj(
        self, 
        id: Optional[str] = None, 
        slug: Optional[str] = None, 
        prefetch_related: Optional[List[str]] = None
    ):
        filters = {}
        if hasattr(self.model, "is_deleted"):
            filters["is_deleted"] = False
        if id:
            filters["id"] = id
        if slug:
            filters["slug"] = slug

        query = self.model.filter(**filters)

        if prefetch_related:
            query = query.prefetch_related(*prefetch_related)

        return await query.first()
    
    async def trash(self, id: str):
        obj = await self.model.get_or_none(id=id)
        if not obj:
            return None 
        if not hasattr(obj, "is_deleted"):
            raise AttributeError(f"{self.model.__name__} does not have 'is_deleted' field")

        obj.is_deleted = True
        await obj.save()
        return obj