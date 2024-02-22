from enum import Enum, auto


class FrameEffect(Enum):
    LEGENDARY = "legendary"  # The cards have a legendary crown
    MIRACLE = "miracle"  # The miracle frame effect
    NYXTOUCHED = "nyxtouched"  # The Nyx-touched frame effect
    DRAFT = "draft"  # The draft-matters frame effect
    DEVOID = "devoid"  # The Devoid frame effect
    TOMBSTONE = "tombstone"  # The Odyssey tombstone mark
    COLORSHIFTED = "colorshifted"  # A colorshifted frame
    INVERTED = "inverted"  # The FNM-style inverted frame
    SUNMOONDFC = "sunmoondfc"  # The sun and moon transform marks
    COMPASSLANDDFC = "compasslanddfc"  # The compass and land transform marks
    ORIGINPWDFC = "originpwdfc"  # The Origins and planeswalker transform marks
    MOONELDRAZIDFC = "mooneldrazidfc"  # The moon and Eldrazi transform marks
    WAXINGANDWANINGMOONDFC = "waxingandwaningmoondfc"  # The waxing and waning crescent moon transform marks
    SHOWCASE = "showcase"  # A custom Showcase frame
    EXTENDEDART = "extendedart"  # An extended art frame
    COMPANION = "companion"  # The cards have a companion frame
    ETCHED = "etched"  # The cards have an etched foil treatment
    SNOW = "snow"  # The cards have the snowy frame effect
    LESSON = "lesson"  # The cards have the Lesson frame effect
    SHATTEREDGLASS = "shatteredglass"  # The cards have the Shattered Glass frame effect
    CONVERTDFC = "convertdfc"  # The cards have More Than Meets the Eye™ marks
    FANDFC = "fandfc"  # The cards have fan transforming marks
    UPSIDEDOWNDFC = "upsidedowndfc"  # The cards have the Upside Down transforming marks
