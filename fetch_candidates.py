from pathlib import Path

from src.api import ApiClient
from src.api.cards import fuzzy, random
import requests
import json

client = ApiClient()


payload = json.loads(
    """{
    "identifiers": [
        {
        "id": "683a5707-cddb-494d-9b41-51b4584ded69"
        },
        {
        "name": "Ancient Tomb"
        },
        {
        "set": "mrd",
        "collector_number": "150"
        }
    ]
    }"""
)
print(payload)
# print(len(payload['identifiers']))
# print(payload['identifiers'])
# print(json.dumps(payload, indent=4))
# # print(json.dumps(payload))
# resp = requests.post("https://api.scryfall.com/cards/collection", data=payload)
# # resp = requests.post("https://api.scryfall.com/cards/collection", json=json.dumps(payload))
# print(resp)
# print(resp.json())


path = Path("candidates.txt")
with path.open("r") as fp:
    candidates = fp.read().split("\n")


for name in candidates:
    # card = fuzzy(client, name)
    card = random(client)
    print(card.name)
