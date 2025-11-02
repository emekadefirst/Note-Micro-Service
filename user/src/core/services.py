from src.utlities.repository import UserBaseRepository
from src.core.models import User
from src.core.schemas import UserSchema, UserObjectSchema
from src.utlities.hash import PasswordManager


class UserService:
    boa = UserBaseRepository(User)
    password = PasswordManager

    @classmethod
    async def get(cls, id: str) -> UserObjectSchema:
        return await cls.boa.get_obj(id=id)
    
    @classmethod
    async def all(cls):
        return await cls.boa.all()
    
    @classmethod
    async def filter(cls, **kwargs):
        return await cls.boa.filter(**kwargs)
    
    @classmethod
    async def delete(cls, id: str):
        return await cls.boa.trash(id=id)   
    
    @classmethod
    async def create(cls, dto: UserSchema):
        hashed_password = PasswordManager.set_password(dto.password)
        return await cls.boa.model.create(**dto.dict(exclude={"password"}), password=hashed_password)
