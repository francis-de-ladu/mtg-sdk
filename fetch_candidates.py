from pathlib import Path
from typing import Optional
from src.api import ApiClient
from src.api.cards import fuzzy, random, collection
import requests
import json
from itertools import batched
from src.misc import IdentName, Identifier
from pprint import pprint
from src.cards import Card, CardFace
import pandas as pd
import ast

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


path = Path("data/candidates.txt")
with path.open("r") as fp:
    candidate_names = fp.read().splitlines()


path = Path("data/commanders.txt")
with path.open("r") as fp:
    commander_names = fp.read().splitlines()


commander_idents: list[Identifier] = [IdentName(name) for name in commander_names]
candidate_idents: list[Identifier] = [IdentName(name) for name in candidate_names]


commanders: list[Card] = collection(client, commander_idents).data

cards_found: list[Card] = []
not_found: list[dict] = []

for batch in batched(candidate_idents, n=75):
    col = collection(client, batch)
    not_found.extend(col.not_found)
    cards_found.extend(col.data)

for entry in not_found:
    if "name" in entry:
        # TODO: fix requirement to cast to string and parse
        entry = ast.literal_eval(str(entry))
        card: Card = fuzzy(client, entry["name"])
        cards_found.append(card)


def extract_fields(card: Card | CardFace, parent: Optional[Card] = None) -> dict:
    main: Card = parent or card  # type: ignore
    return {
        "name": card.name,
        "parent": None if parent is None else parent.name,
        "type_line": card.type_line,
        "edhrec_rank": main.edhrec_rank,
        "price": f"{main.prices.get('usd', '???')}$",
        "mana_cost": card.mana_cost,
        "power": card.power,
        "toughness": card.toughness or card.loyalty,
        "commander?": main.legalities["commander"],
        "produced_mana": None if main.produced_mana is None else main.produced_mana.as_mana(),
        "oracle_text": card.oracle_text,
    }


def card_to_fields(card: Card) -> list[dict]:
    output = []
    if card.card_faces is None:
        output.append(extract_fields(card))
    else:
        output.extend(extract_fields(face, card) for face in card.card_faces)
    return output

for commander in commanders:
    cards = [card for card in cards_found if card.can_be_commanded_by(commander)]

    # df = pd.DataFrame.from_records(
    #     [
    #         *card_to_fields(card) for card in cards
    #     ]
    # )
    # df = pd.DataFrame.from_records(
    #     [
    #         {
    #             "name": card.name,
    #             "type_line": card.type_line,
    #             "edhrec_rank": card.edhrec_rank,
    #             "price": f"{card.prices.get("usd", "???")}$",
    #             "mana_cost": card.mana_cost,
    #             "power": card.power,
    #             "toughness": card.toughness or card.loyalty,
    #             "commander?": card.legalities["commander"],
    #             "produced_mana": None if card.produced_mana is None else card.produced_mana.as_mana(),
    #             "oracle_text": card.oracle_text,
    #         }
    #         for card in cards
    #     ]
    # )
    df.to_csv(f"out/{commander.name}.csv", index=False)

# card = fuzzy(client, "Ghazghkull, Prophet of the Waaagh!")
# print(card.name)
# print(card.set_name)

# for name in candidates:
#     card = fuzzy(client, name)
#     # card = random(client)
#     print(card.name)
