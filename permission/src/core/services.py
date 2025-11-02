from src.utilities.repository import PermissionBaseRepository
from src.core.schemas import (
    PermssionSchema, 
    PermissionGroupSchema
)
from src.core.models import Permission, PermissionGroup
from fastapi import HTTPException


class PermissionsService:
    boa = PermissionBaseRepository(Permission)

    @classmethod
    async def create(cls, dto: PermssionSchema):
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
    async def update(cls, id: str, dto: PermssionSchema):
        obj = await cls.boa.get_obj(id=id)
        if not obj:
            raise HTTPException(status_code=404, detail="Permission not found")

        update_data = dto.dict(exclude_unset=True, exclude_none=True)
        for field, value in update_data.items():
            setattr(obj, field, value)
        return await obj.save()
    

class PermissionGroupService:
    boa = PermissionBaseRepository(PermissionGroup)

    @classmethod
    async def verify_permission_by_id(cls, id: str):
        """Ensure the permission exists before use"""
        perm = await PermissionsService.get(id=id)
        if not perm:
            raise HTTPException(status_code=400, detail=f"Invalid permission ID: {id}")
        return perm
    
    @classmethod
    async def list(cls):
        return await cls.boa.all(prefetch_related=["permissions"])

    @classmethod
    async def get(cls, id: str):
        return await cls.boa.get_obj(id=id, prefetch_related=["permissions"])

    @classmethod
    async def delete(cls, id: str):
        return await cls.boa.trash(id=id)
    
    @classmethod
    async def create(cls, dto: PermissionGroupSchema):
        prm_grp = await cls.boa.model.create(**dto.dict(exclude={"permission_ids"}))

        if dto.permission_ids:
            for perm_id in dto.permission_ids:
                perm = await cls.verify_permission_by_id(perm_id)
                await prm_grp.permissions.add(perm)

        return prm_grp 

    @classmethod
    async def update(cls, id: str, dto: PermissionGroupSchema):
        prm_grp = await cls.boa.get_obj(id=id)
        if not prm_grp:
            raise HTTPException(status_code=404, detail="Permission group not found")

        update_data = dto.dict(exclude_unset=True, exclude_none=True, exclude={"permission_ids"})
        for field, value in update_data.items():
            setattr(prm_grp, field, value)
        if dto.permission_ids is not None:
            await prm_grp.permissions.clear()
            for pid in dto.permission_ids:
                perm = await cls.verify_permission_by_id(pid)
                await prm_grp.permissions.add(perm)

        return await prm_grp.save()
    
