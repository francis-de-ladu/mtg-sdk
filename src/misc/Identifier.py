from abc import ABC, abstractmethod
from enum import Enum
from typing import Optional, override
from uuid import UUID


class Kind(Enum):
    SCRYFALL = "id"
    MTGO = "mtgo_id"
    MULTIVERSE = "multiverse_id"
    ORACLE = "oracle_id"
    ILLUSTRATION = "illustration_id"


class Identifier(ABC):
    @abstractmethod
    def to_dict(self) -> dict[str, str]:
        pass


class IdentId(Identifier):
    def __init__(
        self,
        id: UUID | str | int,
        kind: Optional[str | Kind] = Kind.SCRYFALL,
    ):
        self.id = str(id)
        self.kind = Kind(kind).value

    @override
    def to_dict(self) -> dict[str, str]:
        return {self.kind: self.id}


class IdentName(Identifier):
    def __init__(self, name: str, set: Optional[str] = None):
        self.name = name
        self.set = set

    @override
    def to_dict(self) -> dict[str, str]:
        output = {"name": self.name}
        if self.set is not None:
            output["set"] = self.set
        return output


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
