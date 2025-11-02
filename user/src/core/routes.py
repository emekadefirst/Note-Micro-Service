from fastapi import APIRouter
from src.core.schemas import UserSchema
from src.core.services import UserService

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/")
async def create_user(dto: UserSchema):
    return await UserService.create(dto)


@router.get("/{id}")
async def get_user(id: str):
    return await UserService.get(id)


@router.get("/")
async def get_all_users():
    return await UserService.all()


@router.get("/filter/")
async def filter_users(**kwargs):
    return await UserService.filter(**kwargs)


@router.delete("/{id}")
async def delete_user(id: str):
    return await UserService.delete(id)
