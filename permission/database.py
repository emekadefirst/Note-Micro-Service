from tortoise import Tortoise
from auth.configs import DBURL 


TORTOISE_ORM = {
    "connections": {
        "default": {
            "engine": "tortoise.backends.aiosqlite",
            "credentials": {
                "file_path": DBURL.replace("sqlite://", ""),  # remove scheme to get the file path
            },
        }
    },
    "apps": {
        "models": {
            "models": ["src.core.models", "aerich.models"],
            "default_connection": "default",
        }
    },
    "use_tz": True,
    "timezone": "Africa/Lagos",
    "minsize": 5,
    "maxsize": 50,
    "max_queries": 500,
    "max_inactive_connection_lifetime": 600.0,
}
