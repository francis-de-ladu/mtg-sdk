from enum import Enum

from src.api import ApiClient, CardsEndpoint, List
from src.cards.Card import Card


class Identifier(Enum):
    # Finds a card with the specified Scryfall id.
    ID = "ID"
    # Finds a card with the specified mtgo_id or mtgo_foil_id.
    MTGO_ID = "MTGO_ID"
    # Finds a card with the specified value among its multiverse_ids.
    MULTIVERSE_ID = "MULTIVERSE_ID"
    # Finds the newest edition of cards with the specified oracle_id.
    ORACLE_ID = "ORACLE_ID"
    # Finds the preferred scans of cards with the specified illustration_id.
    ILLUSTRATION_ID = "ILLUSTRATION_ID"
    # Finds the newest edition of a card with the specified name.
    NAME = "NAME"
    # Finds a card matching the specified name and set.
    NAME__SET = "NAME,SET"
    # Finds a card with the specified collector_number and set.
    # Note that collector numbers are strings.
    COLLECTOR_NUMBER__SET = "COLLECTOR_NUMBER, SET"


def collection(
    client: ApiClient,
    identifiers: list[Identifier],
    *,
    pretty: bool = False,
):  # -> List[Card]:
    identifiers = [Identifier(ident) for ident in identifiers]

    params = {
        "pretty": pretty,
    }

    # candidates = client.post(CardsEndpoint.COLLECTION, List[Card], params)
    # return candidates
