from abc import ABC, abstractmethod
from typing import Optional, override
from uuid import UUID


class Identifier(ABC):
    @abstractmethod
    def to_dict(self) -> dict[str, str]:
        pass


class IdentId(Identifier):
    def __init__(self, id: UUID | str | int, kind: str):
        self.id = str(id)
        self.kind = kind

    @override
    def to_dict(self) -> dict[str, str]:
        return {self.kind: self.id}


class IdentName(Identifier):
    def __init__(self, name: str, set: Optional[str] = None):
        self.name = name
        self.set = set

    @override
    def to_dict(self) -> dict[str, str]:
        if self.set is None:
            return {
                "name": self.name,
            }
        else:
            return {
                "name": self.name,
                "set": self.set,
            }


class IdentNumber(Identifier):
    def __init__(self, number: str, set: str):
        self.number = number
        self.set = set

    @override
    def to_dict(self) -> dict[str, str]:
        return {
            "collector_number": self.number,
            "set": self.set,
        }
