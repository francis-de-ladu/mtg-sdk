from enum import Enum
from uuid import UUID

from loguru import logger

from src.api import ApiClient, CardsEndpoint
from src.cards.Card import Card


class Kind(Enum):
    SCRYFALL = ""
    MTGO = "mtgo"
    ARENA = "arena"
    TCGPLAYER = "tcgplayer"
    CARDMARKET = "cardmarket"
    MULTIVERSE = "multiverse"


class Format(Enum):
    JSON = "json"
    TEXT = "text"
    IMAGE = "image"


class Face(Enum):
    FRONT = None
    BACK = "back"


class Version(Enum):
    SMALL = "small"
    NORMAL = "normal"
    LARGE = "large"
    PNG = "png"
    ART_CROP = "art_crop"
    BORDER_CROP = "border_crop"


def _id(
    client: ApiClient,
    card_id: UUID | str | int,
    *,
    kind: str | Kind = Kind.SCRYFALL,
    fmt: str | Format = Format.JSON,
    face: str | Face = Face.FRONT,
    version: str | Version = Version.LARGE,
    pretty: bool = False,
) -> Card:
    kind = Kind(kind).value
    fmt = Format(fmt).value
    face = Face(face).value
    version = Version(version).value

    if fmt != Format.IMAGE:
        if face == Face.BACK:
            logger.warning("Requesting for `back` face only works with `image` format.")

    params = {
        "format": fmt,
        "face": face,
        "version": version,
        "pretty": pretty,
    }

    card = client.get(CardsEndpoint.ID, Card, params, id=card_id)
    return card
