from dataclasses import dataclass
from datetime import date
from functools import cached_property
from typing import override
from uuid import UUID

from urllib3.util import Url

from ..base import Base
from ..misc import Color, FrameEffect
from .CardFace import CardFace
from .Preview import Preview
from .RelatedCard import RelatedCard


@dataclass(frozen=True, kw_only=True)
class Card(Base):
    ### Core Card Fields ###
    # This card's Arena ID, if any. A large percentage of cards are not available on Arena and do not have this ID.
    arena_id: int = None
    # This card's ID on Cardmarket's API, also known as the idProduct.
    cardmarket_id: int = None
    # A unique ID for this card in Scryfall's database.
    id: UUID
    # A language code for this printing.
    lang: str
    # A code for this card's layout.
    layout: str
    # This card's foil Magic Online ID (also known as the Catalog ID), if any. A large percentage of cards are not available on Magic Online and do not have this ID.
    mtgo_foil_id: int = None
    # This card's Magic Online ID (also known as the Catalog ID), if any. A large percentage of cards are not available on Magic Online and do not have this ID.
    mtgo_id: int = None
    # This card's multiverse IDs on Gatherer, if any, as an array of integers. Note that Scryfall includes many promo cards, tokens, and other esoteric objects that do not have these identifiers.
    multiverse_ids: list[int] = None
    # A content type for this object, always card.
    object: str
    # A unique ID for this card's oracle identity. This value is consistent across reprinted card editions, and unique among different cards with the same name (tokens, Unstable variants, etc). Always present except for the reversible_card layout where it will be absent; oracle_id will be found on each face instead.
    oracle_id: UUID = None
    # A link to where you can begin paginating all re/prints for this card on Scryfall's API.
    prints_search_uri: Url
    # A link to this card's rulings list on Scryfall's API.
    rulings_uri: Url
    # A link to this card's permapage on Scryfall's website.
    scryfall_uri: Url
    # This card's ID on TCGplayer's API, for its etched version if that version is a separate product.
    tcgplayer_etched_id: int = None
    # This card's ID on TCGplayer's API, also known as the productId.
    tcgplayer_id: int = None
    # A link to this card object on Scryfall's API.
    uri: Url

    # ### Gameplay Fields ###
    # If this card is closely related to other cards, this property will be an array with Related Card Objects.
    all_parts: list[RelatedCard] = None
    # An array of Card Face objects, if this card is multifaced.
    card_faces: list[CardFace] = None
    # The card's mana value. Note that some funny cards have fractional mana costs.
    cmc: float
    # This card's color identity.
    color_identity: Color
    # The colors in this card's color indicator, if any. A null value for this field indicates the card does not have one.
    color_indicator: Color = None
    # This card's colors, if the overall card has colors defined by the rules. Otherwise the colors will be on the card_faces objects, see below.
    colors: Color = None
    # This face's defense, if any.
    defense: str = None
    # This card's overall rank/popularity on EDHREC. Not all cards are ranked.
    edhrec_rank: int = None
    # This card's hand modifier, if it is Vanguard card. This value will contain a delta, such as -1.
    hand_modifier: str = None
    # An array of keywords that this card uses, such as 'Flying' and 'Cumulative upkeep'.
    keywords: list[str]
    # # An object describing the legality of this card across play formats. Possible legalities are legal, not_legal, restricted, and banned.
    legalities: dict[str, str]
    # This card's life modifier, if it is Vanguard card. This value will contain a delta, such as +2.
    life_modifier: str = None
    # This loyalty if any. Note that some cards have loyalties that are not numeric, such as X.
    loyalty: str = None
    # The mana cost for this card. This value will be any empty string "" if the cost is absent. Remember that per the game rules, a missing mana cost and a mana cost of {0} are different values. Multi-faced cards will report this value in card faces.
    mana_cost: str = None
    # The name of this card. If this card has multiple faces, this field will contain both names separated by ␣//␣.
    name: str
    # The Oracle text for this card, if any.
    oracle_text: str = None
    # This card's rank/popularity on Penny Dreadful. Not all cards are ranked.
    penny_rank: int = None
    # This card's power, if any. Note that some cards have powers that are not numeric, such as *.
    power: str = None
    # Colors of mana that this card could produce.
    produced_mana: Color = None
    # True if this card is on the Reserved List.
    reserved: bool
    # This card's toughness, if any. Note that some cards have toughnesses that are not numeric, such as *.
    toughness: str = None
    # The type line of this card.
    type_line: str

    ### Print Fields ###
    # The name of the illustrator of this card. Newly spoiled cards may not have this field yet.
    artist: str = None
    # The IDs of the artists that illustrated this card. Newly spoiled cards may not have this field yet.
    artist_ids: list[UUID] = None
    # The lit Unfinity attractions lights on this card, if any.
    attraction_lights: list = None
    # Whether this card is found in boosters.
    booster: bool
    # This card’s border color: black, white, borderless, silver, or gold.
    border_color: str
    # The Scryfall ID for the card back design present on this card.
    card_back_id: UUID = None
    # This card’s collector number. Note that collector numbers can contain non-numeric characters, such as letters or ★.
    collector_number: str
    # True if you should consider avoiding use of this print downstream.
    content_warning: bool = None
    # True if this card was only released in a video game.
    digital: bool
    # An array of computer-readable flags that indicate if this card can come in foil, nonfoil, or etched finishes.
    finishes: list[str]
    # The just-for-fun name printed on the card (such as for Godzilla series cards).
    flavor_name: str = None
    # The flavor text, if any.
    flavor_text: str = None
    # True if this card is foil.
    foil: bool
    # This card’s frame effects, if any.
    frame_effects: list[FrameEffect] = None
    # This card’s frame layout.
    frame: str
    # True if this card’s artwork is larger than normal.
    full_art: bool
    # A list of games that this card print is available in, paper, arena, and/or mtgo.
    games: list[str]
    # True if this card’s imagery is high resolution.
    highres_image: bool
    # A unique identifier for the card artwork that remains consistent across reprints. Newly spoiled cards may not have this field yet.
    illustration_id: UUID = None
    # A computer-readable indicator for the state of this card’s image, one of missing, placeholder, lowres, or highres_scan.
    image_status: str
    # An object listing available imagery for this card. See the Card Imagery article for more information.
    image_uris: dict[str, Url] = None
    # True if this card is nonfoil.
    nonfoil: bool
    # True if this card is oversized.
    oversized: bool
    # An object containing daily price information for this card, including usd, usd_foil, usd_etched, eur, eur_foil, eur_etched, and tix prices, as strings.
    prices: dict[str, float]
    # The localized name printed on this card, if any.
    printed_name: str = None
    # The localized text printed on this card, if any.
    printed_text: str = None
    # The localized type line printed on this card, if any.
    printed_type_line: str = None
    # True if this card is a promotional print.
    promo: bool
    # An array of strings describing what categories of promo cards this card falls into.
    promo_types: list[str] = None
    # An object providing URIs to this card’s listing on major marketplaces. Omitted if the card is unpurchaseable.
    purchase_uris: dict[str, Url] = None
    # This card’s rarity. One of common, uncommon, rare, special, mythic, or bonus.
    rarity: str
    # An object providing URIs to this card’s listing on other Magic: The Gathering online resources.
    related_uris: dict[str, Url]
    # The date this card was first released.
    released_at: date
    # True if this card is a reprint.
    reprint: bool
    # A link to this card’s set on Scryfall’s website.
    scryfall_set_uri: Url
    # This card’s full set name.
    set_name: str
    # A link to where you can begin paginating this card’s set on the Scryfall API.
    set_search_uri: Url
    # The type of set this printing is in.
    set_type: str
    # A link to this card’s set object on Scryfall’s API.
    set_uri: Url
    # This card’s set code.
    set: str
    # This card’s Set object UUID.
    set_id: UUID
    # True if this card is a Story Spotlight.
    story_spotlight: bool
    # True if the card is printed without text.
    textless: bool
    # Whether this card is a variation of another printing.
    variation: bool
    # The printing ID of the printing this card is a variation of.
    variation_of: UUID = None
    # The security stamp on this card, if any. One of oval, triangle, acorn, circle, arena, or heart.
    security_stamp: str = None
    # This card’s watermark, if any.
    watermark: str = None
    # Information about the card's preview, if any.
    preview: Preview = None

    @classmethod
    def from_dict(cls, data):
        if data["layout"] == "reversible_card":
            data["cmc"] = data["card_faces"][0]["cmc"]
            data["type_line"] = data["card_faces"][0]["type_line"]

        return cls(**data)

    @override
    @cached_property
    def _types_to_cast(self):
        return {
            date: self._to_date,
            Color: self._to_color,
            Url: self._to_url,
            UUID: self._to_uuid,
            CardFace: self._to_face,
            Preview: self._to_preview,
            RelatedCard: self._to_related,
        }

    def _to_face(self, value):
        return CardFace.from_dict(value)

    def _to_preview(self, value):
        return Preview.from_dict(value)

    def _to_related(self, value):
        return RelatedCard.from_dict(value)
