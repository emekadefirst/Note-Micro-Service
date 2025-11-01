from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID
from datetime import datetime

class NoteSchema(BaseModel):
    title: Optional[str] = Field(None, max_length=150)
    description: Optional[str] = None
    user_id: Optional[str] = None


class NoteSchemaObject(BaseModel):
    id: UUID
    title: str = Field(..., max_length=150)
    description: str = None
    user_id: UUID
    created_at: Optional[datetime]
    updated_at: Optional[datetime]