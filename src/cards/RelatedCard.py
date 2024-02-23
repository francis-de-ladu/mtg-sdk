from dataclasses import dataclass
from uuid import UUID

from urllib3.util import Url

from src.base import Base


@dataclass(frozen=True, kw_only=True)
class RelatedCard(Base):
    # An unique ID for this card in Scryfall's database.
    id: UUID
    # A content type for this object, always related_card.
    object: str
    # A field explaining what role this card plays in this relationship, one of token, meld_part,
    # meld_result, or combo_piece.
    component: str
    # The name of this particular related card.
    name: str
    # The type line of this card.
    type_line: str
    # A URI where you can retrieve a full object describing this card on Scryfall's API.
    uri: Url
