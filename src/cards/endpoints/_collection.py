import os
from enum import Enum

import requests
from loguru import logger

from src.cards.Card import Card

CARD_ENDPOINT = "https://api.scryfall.com/cards"


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


def collection(
    *,
    exact: str = None,
    fuzzy: str = None,
    set: str = None,
    fmt: Format = Format.JSON,
    face: Face = Face.FRONT,
    version: Version = Version.LARGE,
    pretty: bool = False,
):
    assert (exact is None) != (fuzzy is None), "Exactly one of (`exact`|`fuzzy`) must be provided."

    if fmt != Format.IMAGE:
        if face == Face.BACK:
            logger.warn("Requesting for `back` face only works with `image` format.")

    url = os.path.join(CARD_ENDPOINT, "named")

    resp = requests.get(
        url,
        {
            "exact": exact,
            "fuzzy": fuzzy,
            "set": set,
            "fmt": fmt,
            "face": face,
            "version": version,
            "pretty": pretty,
        },
    )
    from pprint import pprint

    print(resp.status_code)
    data = resp.json()
    pprint(data)
    card = Card.from_dict(data)
    pprint(card)
