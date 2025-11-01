from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "notes" (
    "id" CHAR(36) NOT NULL PRIMARY KEY,
    "title" VARCHAR(150),
    "body" TEXT,
    "user_id" CHAR(36) NOT NULL,
    "created_at" TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMP,
    "is_deleted" INT NOT NULL DEFAULT 0
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSON NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """


MODELS_STATE = (
    "eJzVl2tP2zAUhv9KlE9MYqiUctE0TWqhG51oM0G6IRCK3NhNLRy7JM5ohfjv83FzT5u1sA"
    "n6pWrOJfZ5jh2/fjJ9gQkL9wZCEvOT8WRy5MOfgn3XMNF0mlnBINGI6UCuIrQFjUIZIFcq"
    "4xixkCgTJqEb0KmkgisrjxgDo3BVIOVeZoo4fYiII4VH5IQEynF7p8yUYzJTL48fp/fOmB"
    "KGC/OkGMbWdkfOp9o2HPbOvupIGG7kuIJFPs+ip3M5ETwNjyKK9yAHfB7hJECS4FwZMMu4"
    "3MS0mLEyyCAi6VRxZsBkjCIGMMzP44i7wMDQI8FP64u5AR5XcEBLuQQWT8+LqrKatdWEoU"
    "7P25c7B0cfdJUilF6gnZqI+awTkUSLVM01AympZKTK8nSCguUs04QSTjXVNUDGmFKOSUgG"
    "MltECcmE0MuwmT6aOYxwT07U4/5ho4bjz/alRqmiNEuhFvZiuQ9iV3PhA6YZw5HA8ypCm8"
    "zkcoRJ/JYQrAFmd69tmLMfhg8sz2mn377WCP157LmwBt+S8BzX0wurU8IZhSRwNtvguZR/"
    "ucvflO1fN3VGzA0IVOUgWYV2pjyS+mQ5uGJmiR2OU/eSP+9yeZqqBGxxNo9Hr1uuvX73ym"
    "73fxTW7Fnb7oKnWViviXXnqPQpSF9i/OrZ5wY8GjfWoFvuUxpn35gwJxRJ4XDx6CCcOzAS"
    "awKmuBOm+IV9LWZuZV+3pI9J2bWNpKGjFBQBupVGdoRgBPEVyqWQWOrjSGX+r8/aplpu/e"
    "Z1LOui0LdOr3woDPudrjqFdcNUENUi1ewNbPXdA0k4vs9pGTCMkHv/iALsVDyiKVbFVl1+"
    "0y9bEEeeRgR1QlWxQm6TgLoTc4l2jj216hllMe9GPvf4Crmy9FxVjS4vvfgT8TrZ/MqzwI"
    "NRPjb3W8etk4Oj1okK0TNJLcc1K3OxwOrU8m8ShDClDfRyLuVFeu8NRElRMjcPD9eQzCpq"
    "pWTWvqJiga2xAcQ4fDsB7jfWunM0au4cjcqdQ40oCV+iC75fWYMVWi9LKYEcclXgLaau3D"
    "UYDeXd+8RaQxGqrr+IlO8cpVMeXtB56+Pl+Q/C3p1O"
)
