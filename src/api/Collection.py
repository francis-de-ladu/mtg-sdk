from dataclasses import dataclass

from ..base import Base
from ..cards import Card


@dataclass(frozen=True, kw_only=True)
class Collection(Base):
    # A content type for this object, always list.
    object: str
    # Identifiers that are not found will be returned in this array.
    not_found: list[dict[str, str]]
    # Cards found will be returned in the order that they were requested in this array.
    data: list[Card.from_dict]  # type: ignore[valid-type]
