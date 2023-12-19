from enum import Enum


class Enum(str, Enum):
    def __str__(self) -> str:
        return str.__str__(self)
