from typing import TypeVar

from src.api import ApiClient, CardsEndpoint, Collection
from src.misc import Identifier

Ident = TypeVar("Ident", bound=Identifier)


def collection(
    client: ApiClient,
    identifiers: list[Ident],
    *,
    pretty: bool = False,
) -> Collection:
    params = {
        "pretty": pretty,
    }

    payload = {"identifiers": [ident.to_dict() for ident in identifiers]}

    candidates = client.post(CardsEndpoint.COLLECTION, Collection, params, payload)
    return candidates
