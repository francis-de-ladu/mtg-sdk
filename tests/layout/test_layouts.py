import unittest

from pathlib import Path
import json
from src.cards.Card import Card

from tqdm import tqdm
layout_dir = Path("./tests/layout/data")
import time

class LayoutTestCase(unittest.TestCase):
    def test_layouts(self):
        files = list(layout_dir.iterdir())
        desc_len = max(len(file.stem) for file in files)

        progress = tqdm(files)
        for file in progress:
            progress.desc = f"{file.stem:^{desc_len}}"
            time.sleep(0.02)
            with file.open('r') as fp:
                resp = json.load(fp)
            
            card = Card.from_dict(resp)
            self.assertIsInstance(card, Card)

if __name__ == '__main__':
    unittest.main()