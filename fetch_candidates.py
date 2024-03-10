from pathlib import Path

from src.api import ApiClient
from src.api.cards import fuzzy, random, collection
import requests
import json
from itertools import batched
from src.misc import IdentName

client = ApiClient()


# payload = {
#     "identifiers": [
#         # {"id": "683a5707-cddb-494d-9b41-51b4584ded69"},
#         {"name": "Ancient Tomb"},
#         {"name": "Lollipop"},
#         # {"set": "mrd", "collector_number": "150"},
#     ]
# }

# resp = requests.post("https://api.scryfall.com/cards/collection", json=payload)
# print(resp.json())


path = Path("candidates.txt")
with path.open("r") as fp:
    candidates = fp.read().splitlines()



idents = [IdentName(name) for name in candidates]
collection(client, idents[:75])
from pprint import pprint
for batch in batched(idents, n=75):
    # pprint([sup.to_dict() for sup in batch])
    col = collection(client, batch)
    pprint(col.not_found)


# card = fuzzy(client, "Ghazghkull, Prophet of the Waaagh!")
# print(card.name)
# print(card.set_name)

# for name in candidates:
#     card = fuzzy(client, name)
#     # card = random(client)
#     print(card.name)
