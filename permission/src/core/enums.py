from enum import Enum


class Action(str, Enum):
    CREATE = "create"
    READ = "read"
    UPDATE = "update"
    DELETE = "delete"


class Module(str, Enum):
    NOTE = "note"
    USER = "user"
    PERMISSION = "permission"