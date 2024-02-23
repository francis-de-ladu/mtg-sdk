from enum import Enum


class Endpoint(Enum):
    pass


class CardsEndpoint(Endpoint):
    ID = "{id}"
    NAMED = "named"
    SEARCH = "search"
    RANDOM = "random"
    AUTOCOMPLETE = "autocomplete"
    COLLECTION = "collection"
    MULTIVERSE = "multiverse/{id}"
    MTGO = "mtgo/{id}"
    ARENA = "arena/{id}"
    TCGPLAYER = "tcgplayer/{id}"
    CARDMARKET = "cardmarket/{id}"
    CODE__NUMBER = "{code}/{number}/en"  # TODO: add support of providing a language


class SetsEndpoint(Endpoint):
    ALL = ""
    ID = "{id}"
    CODE = "code"
    TCGPLAYER = "tcgplayer/{id}"
