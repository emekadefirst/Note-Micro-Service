from pydantic import BaseModel, Field, EmailStr
from typing import List, Optional
from uuid import UUID
from datetime import datetime


class UserSchema(BaseModel):
    first_name: str = Field(None, max_length=50, description="The user's first name")
    last_name: str = Field(None, max_length=50, description="The user's last name")
    email: EmailStr = Field(None, max_length=50, description="The user's email address")
    password: str = Field(None, max_length=150, description="The user's password")



class UserObjectSchema(UserSchema):
    id: UUID = Field(..., description="The unique identifier of the user")
    first_name: str = Field(..., max_length=50, description="The user's first name")
    last_name: str = Field(..., max_length=50, description="The user's last name")
    email: EmailStr = Field(..., max_length=50, description="The user's email address")
    password: str = Field(..., max_length=150, description="The user's password")
    is_admin: bool 
    is_deleted: bool
    permission_groups: List[str]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

