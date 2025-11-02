from src.configs.env import DBURL


if DBURL.startswith("sqlite://"):
    db_url = DBURL
elif DBURL.startswith("aiosqlite://"):
    db_url = DBURL
else:
    db_url = f"sqlite://{DBURL}"
TORTOISE_ORM = {
    "connections": {
        "default": db_url          
    },
    "apps": {
        "models": {
            "models": ["src.core.models", "aerich.models"],
            "default_connection": "default",
        }
    },
    "use_tz": False,
    "timezone": "UTC",
}