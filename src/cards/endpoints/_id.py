import os
from enum import Enum
from uuid import UUID

import requests
from loguru import logger

from src.cards.Card import Card

CARD_ENDPOINT = "https://api.scryfall.com/cards"


class Kind(Enum):
    SCRYFALL = ""
    MTGO = "mtgo"
    ARENA = "arena"
    TCGPLAYER = "tcgplayer"
    CARDMARKET = "cardmarket"
    MULTIVERSE = "multiverse"


class Format(Enum):
    JSON = "json"
    CSV = "csv"
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
    card_id: UUID | int,
    *,
    kind: Kind = Kind.SCRYFALL,
    fmt: Format = Format.JSON,
    face: Face = Face.FRONT,
    version: Version = Version.LARGE,
    pretty: bool = False,
) -> Card:
    kind = Kind(kind).value
    fmt = Format(fmt).value
    face = Face(face).value
    version = Version(version).value

    if fmt != Format.IMAGE:
        if face == Face.BACK:
            logger.warn("Requesting for `back` face only works with `image` format.")

    params = {
        "fmt": fmt,
        "face": face,
        "version": version,
        "pretty": pretty,
    }

    url = os.path.join(CARD_ENDPOINT, kind.value, str(card_id))
    resp = requests.get(url, params)
    logger.info(f"{params}, {resp}")

    card = Card.from_dict(resp.json())
    return card
