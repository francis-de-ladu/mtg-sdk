from dataclasses import dataclass
from typing import Generic, Optional, TypeVar

from urllib3.util import Url

from src.base import Base

T = TypeVar("T", bound=Base)


@dataclass(frozen=True, kw_only=True)
class List(Base, Generic[T]):
    # A content type for this object, always list.
    object: str
    # An array of the requested objects, in a specific order.
    data: list[T]
    # True if this List is paginated and there is a page beyond the current page.
    has_more: bool
    # If there is a page beyond the current page, this field will contain a full API URI to that page.
    # You may submit a HTTP GET request to that URI to continue paginating forward on this List.
    next_page: Optional[Url] = None
    # If this is a list of Card objects, this field will contain the total number of cards found across all pages.
    total_cards: Optional[int] = None
    # An array of human-readable warnings issued when generating this list, as strings.
    # Warnings are non-fatal issues that the API discovered with your input.
    # In general, they indicate that the List will not contain the all of the information you requested.
    # You should fix the warnings and re-submit your request.
    warnings: Optional[list[str]] = None
