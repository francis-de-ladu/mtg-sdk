from enum import Enum


class Layout(Enum):
    NORMAL = "normal"  # A standard Magic card with one face
    SPLIT = "split"  # A split-faced card
    FLIP = "flip"  # Cards that invert vertically with the flip keyword
    TRANSFORM = "transform"  # Double-sided cards that transform
    MODAL_DFC = "modal_dfc"  # Double-sided cards that can be played either-side
    MELD = "meld"  # Cards with meld parts printed on the back
    LEVELER = "leveler"  # Cards with Level Up
    CLASS = "class"  # Class-type enchantment cards
    CASE = "case"  # Case-type enchantment cards
    SAGA = "saga"  # Saga-type cards
    ADVENTURE = "adventure"  # Cards with an Adventure spell part
    MUTATE = "mutate"  # Cards with Mutate
    PROTOTYPE = "prototype"  # Cards with Prototype
    BATTLE = "battle"  # Battle-type cards
    PLANAR = "planar"  # Plane and Phenomenon-type cards
    SCHEME = "scheme"  # Scheme-type cards
    VANGUARD = "vanguard"  # Vanguard-type cards
    TOKEN = "token"  # Token cards
    DOUBLE_FACED_TOKEN = "double_faced_token"  # Tokens with another token printed on the back
    EMBLEM = "emblem"  # Emblem cards
    AUGMENT = "augment"  # Cards with Augment
    HOST = "host"  # Host-type cards
    ART_SERIES = "art_series"  # Art Series collectable double-faced cards
    REVERSIBLE_CARD = "reversible_card"  # A Magic card with two sides that are unrelated
