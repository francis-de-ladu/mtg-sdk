import os
from enum import Enum
from typing import Any

import requests
from loguru import logger

from src.cards.Card import Card

CARD_ENDPOINT = "https://api.scryfall.com/cards"


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
    query: str,
    set: str = None,
    fmt: Format = Format.JSON,
    face: Face = Face.FRONT,
    version: Version = Version.LARGE,
    pretty: bool = False,
) -> Card:
    return _named(
        {
            "exact": query,
            "set": set,
            "fmt": fmt,
            "face": face,
            "version": version,
            "pretty": pretty,
        }
    )


def fuzzy(
    query: str,
    set: str = None,
    fmt: Format = Format.JSON,
    face: Face = Face.FRONT,
    version: Version = Version.LARGE,
    pretty: bool = False,
) -> Card:
    return _named(
        {
            "fuzzy": query,
            "set": set,
            "fmt": fmt,
            "face": face,
            "version": version,
            "pretty": pretty,
        }
    )


def _named(params: dict[str, Any]) -> Card:
    params["fmt"] = Format(params["fmt"]).value
    params["face"] = Face(params["face"]).value
    params["version"] = Version(params["version"]).value

    if params["fmt"] != Format.IMAGE:
        if params["face"] == Face.BACK:
            logger.warn("Requesting for `back` face only works with `image` format.")

    url = os.path.join(CARD_ENDPOINT, "named")
    resp = requests.get(url, params)
    logger.info(f"{params}, {resp}")

    card = Card.from_dict(resp.json())
    return card
