import uvicorn
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from fastapi.middleware.gzip import GZipMiddleware
from src.core.routes import note_router
from tortoise.contrib.fastapi import register_tortoise
from src.core.database import TORTOISE_ORM


app = FastAPI(
    title="Note Manager Service",
    description="Manages Note",
    version="1.0.0",
    default_response_class=ORJSONResponse, 
)


app.add_middleware(
    GZipMiddleware,
    minimum_size=1000  
)

register_tortoise(
    app,
    config=TORTOISE_ORM,
    generate_schemas=True,
    add_exception_handlers=True,
)

app.include_router(note_router)
@app.get("/", tags=["Health"])
async def root():
    return {"message": "Note Service is running 🚀"}


def run_server():
    uvicorn.run("src.scripts.main:app", host="0.0.0.0", port=8001, reload=True)


def run_prod():
    uvicorn.run("src.scripts.main:app", host="0.0.0.0", port=8001, reload=False, workers=2)

