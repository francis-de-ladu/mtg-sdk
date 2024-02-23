from enum import Enum
from typing import Optional

from loguru import logger

from src.api import ApiClient, CardsEndpoint
from src.cards.Card import Card


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


def random(
    client: ApiClient,
    query: Optional[str] = None,
    *,
    fmt: str | Format = Format.JSON,
    face: str | Face = Face.FRONT,
    version: str | Version = Version.LARGE,
    pretty: bool = False,
) -> Card:
    fmt = Format(fmt).value
    face = Face(face).value
    version = Version(version).value

    if fmt != Format.IMAGE:
        if face == Face.BACK:
            logger.warning("Requesting for `back` face only works with `image` format.")

    params = {
        "q": query,
        "format": fmt,
        "face": face,
        "version": version,
        "pretty": pretty,
    }

    card = client.get(CardsEndpoint.RANDOM, Card, params)
    return card
