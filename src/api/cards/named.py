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


def exact(
    client: ApiClient,
    query: str,
    set: Optional[str] = None,
    fmt: str | Format = Format.JSON,
    face: str | Face = Face.FRONT,
    version: str | Version = Version.LARGE,
    pretty: bool = False,
) -> Card:
    return _named(
        client,
        {
            "exact": query,
            "set": set,
            "format": fmt,
            "face": face,
            "version": version,
            "pretty": pretty,
        },
    )


def fuzzy(
    client: ApiClient,
    query: str,
    set: Optional[str] = None,
    fmt: str | Format = Format.JSON,
    face: str | Face = Face.FRONT,
    version: str | Version = Version.LARGE,
    pretty: bool = False,
) -> Card:
    return _named(
        client,
        {
            "fuzzy": query,
            "set": set,
            "format": fmt,
            "face": face,
            "version": version,
            "pretty": pretty,
        },
    )


def _named(client: ApiClient, params: dict) -> Card:
    params["format"] = Format(params["format"]).value
    params["face"] = Face(params["face"]).value
    params["version"] = Version(params["version"]).value

    if params["format"] != Format.IMAGE:
        if params["face"] == Face.BACK:
            logger.warning("Requesting for `back` face only works with `image` format.")

    card = client.get(CardsEndpoint.NAMED, Card, params)
    return card
