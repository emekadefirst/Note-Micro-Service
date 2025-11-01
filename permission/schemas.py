from pydantic import BaseModel, Field
from auth.authServices.enums import Action, Module
from typing import Optional, List
from uuid import UUID
from datetime import datetime

class PermssionSchema(BaseModel):
    action: Optional[Action] = Action.READ
    module: Optional[Module] = None


class PermissionObjectSchema(BaseModel):
    id: UUID
    action: Action
    module: Module
    created_at: Optional[datetime]
    updated_at: Optional[datetime]


class PermissionGroupSchema(BaseModel):
    title: Optional[str] = Field(None, max_length=55)
    permission_ids = Optional[List[str]] = None


class PermissionGroupObjectSchema(BaseModel):
    id: UUID
    title: str = Field(..., max_length=55)
    permissions: List[PermissionObjectSchema]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]