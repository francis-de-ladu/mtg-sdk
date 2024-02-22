from enum import Enum


class Frame(Enum):
    _1993 = "1993"  # The original Magic card frame, starting from Limited Edition Alpha.
    _1997 = "1997"  # The updated classic frame starting from Mirage block
    _2003 = "2003"  # The "modern" Magic card frame, introduced in Eighth Edition and Mirrodin block.
    _2015 = "2015"  # The holofoil-stamp Magic card frame, introduced in Magic 2015.
    FUTURE = "future"  # The frame used on cards from the future
