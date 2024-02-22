from dataclasses import dataclass
from uuid import UUID

from urllib3.util import Url

from ..base import Base
from ..misc.Color import Color


@dataclass(frozen=True, kw_only=True)
class CardFace(Base):
    # The name of the illustrator of this card face. Newly spoiled cards may not have this field yet.
    artist: str = None
    # The ID of the illustrator of this card face. Newly spoiled cards may not have this field yet.
    artist_id: UUID = None
    # The mana value of this particular face, if the card is reversible.
    cmc: float = None
    # The colors in this face's color indicator, if any.
    color_indicator: Color = None
    # This face's colors, if the game defines colors for the individual face of this card.
    colors: Color = None
    # This face's defense, if the game defines colors for the individual face of this card.
    defense: str = None
    # The just-for-fun name printed on this face (such as for Godzilla series cards).
    flavor_name: str = None
    # The flavor text printed on this face, if any.
    flavor_text: str = None
    # A unique identifier for the card face artwork that remains consistent across reprints. Newly spoiled cards may not have this field yet.
    illustration_id: UUID = None
    # An object providing URIs to imagery for this face, if this is a double-sided card. If this card is not double-sided, then the image_uris property will be part of the parent object instead.
    image_uris: dict[str, Url] = None
    # The layout of this card face, if the card is reversible.
    layout: str = None
    # This face's loyalty, if any.
    loyalty: str = None
    # The mana cost for this face. This value will be any empty string "" if the cost is absent. Remember that per the game rules, a missing mana cost and a mana cost of {0} are different values.
    mana_cost: str
    # The name of this particular face.
    name: str
    # A content type for this object, always card_face.
    object: str
    # The Oracle ID of this particular face, if the card is reversible.
    oracle_id: UUID = None
    # The Oracle text for this face, if any.
    oracle_text: str = None
    # This face's power, if any. Note that some cards have powers that are not numeric, such as *.
    power: str = None
    # The localized name printed on this face, if any.
    printed_name: str = None
    # The localized text printed on this face, if any.
    printed_text: str = None
    # The localized type line printed on this face, if any.
    printed_type_line: str = None
    # This face's toughness, if any.
    toughness: str = None
    # The type line of this particular face, if the card is reversible.
    type_line: str = None
    # The watermark on this particulary card face, if any.
    watermark: str = None
