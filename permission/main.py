import uvicorn
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from fastapi.middleware.gzip import GZipMiddleware
from auth.permission.routes import permission_router
from tortoise.contrib.fastapi import register_tortoise
from auth.permission.database import TORTOISE_ORM


app = FastAPI(
    title="Auth Manager Service",
    description="Manages permissions and permission groups for internal auth system.",
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

app.include_router(permission_router)
@app.get("/", tags=["Health"])
async def root():
    return {"message": "Auth Permission Service is running 🚀"}


def run_auth_dev():
    uvicorn.run("src.auth.permission.main:app", host="0.0.0.0", port=8001, reload=True)

def run_auth_prod():
    uvicorn.run("src.auth.permission.main:app", host="0.0.0.0", port=8001, reload=False, workers=2)


