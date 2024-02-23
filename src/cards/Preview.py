from dataclasses import dataclass
from datetime import date

from urllib3.util import Url

from src.base import Base


@dataclass(frozen=True, kw_only=True)
class Preview(Base):
    # The date this card was previewed.
    previewed_at: date
    # A link to the preview for this card.
    source_uri: Url
    # The name of the source that previewed this card.
    source: str
