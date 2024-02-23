from dataclasses import dataclass

from urllib3.util import Url

from src.base import Base


@dataclass(frozen=True, kw_only=True)
class Catalog(Base):
    # A content type for this object, always catalog.
    object: str
    # A link to the current catalog on Scryfall’s API.
    uri: Url
    # The number of items in the data array.
    total_values: int
    # An array of datapoints, as strings.
    data: list[str]
