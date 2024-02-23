from enum import Enum

from src.api import ApiClient, CardsEndpoint, Catalog

from typing import Optional


class Format(Enum):
    JSON = "json"


def autocomplete(
    client: ApiClient,
    query: str,
    *,
    fmt: str | Format = Format.JSON,
    pretty: bool = False,
    include_extras: bool = False,
) -> Catalog:
    fmt = Format(fmt).value

    params = {
        "q": query,
        "format": fmt,
        "pretty": pretty,
        "include_extras": include_extras,
    }

    candidates = client.get(CardsEndpoint.AUTOCOMPLETE, Catalog, params)
    return candidates
