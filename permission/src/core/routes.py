from fastapi import APIRouter, HTTPException
from src.core.schemas import (
    PermssionSchema,
    PermissionObjectSchema,
    PermissionGroupSchema,
    PermissionGroupObjectSchema
)
from src.core.services import PermissionsService, PermissionGroupService

permission_router = APIRouter(
    prefix="/permission",
    tags=["Permissions and Permission Groups"]
)

@permission_router.post("/", response_model=PermissionObjectSchema, status_code=201)
async def create_permission(dto: PermssionSchema):
    return await PermissionsService.create(dto)


@permission_router.get("/", response_model=list[PermissionObjectSchema], status_code=200)
async def list_permissions():
    return await PermissionsService.list()


@permission_router.get("/{id}", response_model=PermissionObjectSchema, status_code=200)
async def get_permission(id: str):
    return await PermissionsService.get(id)


@permission_router.patch("/{id}", response_model=PermissionObjectSchema, status_code=200)
async def update_permission(id: str, dto: PermssionSchema):
    return await PermissionsService.update(id, dto)

@permission_router.delete("/{id}", status_code=204)
async def delete_permission(id: str):
    return await PermissionsService.delete(id)

@permission_router.post("/groups/", response_model=PermissionGroupObjectSchema, status_code=201)
async def create_permission_group(dto: PermissionGroupSchema):
    return await PermissionGroupService.create(dto)

@permission_router.get("/groups/", response_model=list[PermissionGroupObjectSchema], status_code=200)
async def list_permission_groups():
    return await PermissionGroupService.list()


@permission_router.get("/{id}", response_model=PermissionGroupObjectSchema, status_code=200)
async def get_permission_group(id: str):
    group = await PermissionGroupService.get(id)
    if not group:
        raise HTTPException(status_code=404, detail="Permission group not found")
    return group


@permission_router.patch("/groups/{id}", response_model=PermissionGroupObjectSchema, status_code=200)
async def update_permission_group(id: str, dto: PermissionGroupSchema):
    return await PermissionGroupService.update(id, dto)


@permission_router.delete("/groups/{id}", status_code=204)
async def delete_permission_group(id: str):
    return await PermissionGroupService.delete(id)
   

