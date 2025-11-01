from fastapi import APIRouter
from src.core.schemas import NoteSchema, NoteSchemaObject
from src.core.services import NoteService

note_router = APIRouter(
    prefix="/notes",
    tags=["Permissions and Permission Groups"]
)

@note_router.post("/", response_model=NoteSchemaObject, status_code=201)
async def create_note(dto: NoteSchema):
    return await NoteService.create(dto)


@note_router.get("/", response_model=list[NoteSchemaObject], status_code=200)
async def list_note():
    return await NoteService.list()


@note_router.get("/{id}", response_model=NoteSchemaObject, status_code=200)
async def get_note(id: str):
    return await NoteService.get(id)


@note_router.patch("/{id}", response_model=NoteSchemaObject, status_code=200)
async def update_note(id: str, dto: NoteSchemaObject):
    return await NoteService.update(id, dto)


@note_router.delete("/{id}", status_code=204)
async def delete_note(id: str):
    return await NoteService.delete(id)
