import json
from src.cards.Card import Card
from pprint import pprint

from pathlib import Path
folder = Path("tests/layout/data")

for file in folder.iterdir():
    with file.open("r") as fp:
        if not file.as_posix().endswith("reversible_card.json"):
            continue
        resp = json.load(fp)

    card = Card.from_dict(resp)
