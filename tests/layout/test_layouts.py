import unittest

from pathlib import Path
import json
from src.cards.Card import Card


layout_dir = Path("./tests/layout/data")


class LayoutTestCase(unittest.TestCase):
    def test_layouts(self):
        for file in layout_dir.iterdir():
            with file.open('r') as fp:
                resp = json.load(fp)
            
            card = Card.from_dict(resp)
            self.assertIsInstance(card, Card)

if __name__ == '__main__':
    unittest.main()