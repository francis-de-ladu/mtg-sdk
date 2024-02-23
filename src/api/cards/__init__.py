from .autocomplete import autocomplete
from .collection import collection
from .id import _id
from .named import exact, fuzzy
from .random import random
from .search import search

__all__ = [
    "_id",
    "exact",
    "fuzzy",
    "search",
    "random",
    "autocomplete",
    "collection",
]
