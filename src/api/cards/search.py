from enum import Enum
from typing import Optional

from src.api import ApiClient, CardsEndpoint, List
from src.cards.Card import Card


class Unique(Enum):
    # Removes duplicate gameplay objects (cards that share a name and have the same functionality).
    # For example, if your search matches more than one print of Pacifism, only one copy of Pacifism will be returned.
    CARDS = "cards"
    # Returns only one copy of each unique artwork for matching cards.
    # For example, if your search matches more than one print of Pacifism, one card with each different illustration
    # for Pacifism will be returned, but any cards that duplicate artwork already in the results will be omitted.
    ART = "art"
    # Returns all prints for all cards matched (disables rollup).
    # For example, if your search matches more than one print of Pacifism, all matching prints will be returned.
    PRINTS = "prints"


class Order(Enum):
    NAME = "name"  # Sort cards by name, A → Z
    SET = "set"  # Sort cards by their set and collector number: AAA/#1 → ZZZ/#999
    RELEASED = "released"  # Sort cards by their release date: Newest → Oldest
    RARITY = "rarity"  # Sort cards by their rarity: Common → Mythic
    COLOR = "color"  # Sort cards by their color and color identity: WUBRG → multicolor → colorless
    USD = "usd"  # Sort cards by their lowest known U.S. Dollar price: 0.01 → highest, null last
    TIX = "tix"  # Sort cards by their lowest known TIX price: 0.01 → highest, null last
    EUR = "eur"  # Sort cards by their lowest known Euro price: 0.01 → highest, null last
    CMC = "cmc"  # Sort cards by their mana value: 0 → highest
    POWER = "power"  # Sort cards by their power: null → highest
    TOUGHNESS = "toughness"  # Sort cards by their toughness: null → highest
    EDHREC = "edhrec"  # Sort cards by their EDHREC ranking: lowest → highest
    PENNY = "penny"  # Sort cards by their Penny Dreadful ranking: lowest → highest
    ARTIST = "artist"  # Sort cards by their front-side artist name: A → Z
    # Sort cards how podcasts review sets, usually color & CMC, lowest → highest, with Booster Fun cards at the end
    REVIEW = "review"


class Direction(Enum):
    AUTO = "auto"  # Scryfall will automatically choose the most inuitive direction to sort
    ASC = "asc"  # Sort ascending (the direction of the arrows in the previous table)
    DESC = "desc"  # Sort descending (flip the direction of the arrows in the previous table)


class Format(Enum):
    JSON = "json"
    CSV = "csv"


def search(
    client: ApiClient,
    query: str,
    *,
    unique: str | Unique = Unique.CARDS,
    order: str | Order = Order.NAME,
    dir: str | Direction = Direction.AUTO,
    fmt: str | Format = Format.JSON,
    include_extras: bool = False,
    include_multilingual: bool = False,
    include_variations: bool = False,
    pretty: bool = False,
    page: int = 1,
) -> List[Card]:

    unique = Unique(unique).value
    order = Order(order).value
    dir = Direction(dir).value
    fmt = Format(fmt).value

    params = {
        "q": query,
        "unique": unique,
        "order": order,
        "dir": dir,
        "format": fmt,
        "include_extras": include_extras,
        "include_multilingual": include_multilingual,
        "include_variations": include_variations,
        "pretty": pretty,
        "page": page,
    }

    cards = client.get(CardsEndpoint.SEARCH, List[Card], params)
    return cards
