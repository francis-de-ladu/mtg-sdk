from pathlib import Path

from src.api import ApiClient
from src.api.cards import fuzzy, random, collection
import requests
import json

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
    candidates = fp.read().split("\n")


first_75 = candidates[:75]

# idents = [Identifier.NAME.value.format(name=name) for name in first_75]
idents = [IdentName(name) for name in first_75]
# print(idents[0].format(name="lala"))
col = collection(client, idents)
from pprint import pprint
pprint(col.not_found)


# card = fuzzy(client, "Ghazghkull, Prophet of the Waaagh!")
# print(card.name)
# print(card.set_name)

# for name in candidates:
#     card = fuzzy(client, name)
#     # card = random(client)
#     print(card.name)
