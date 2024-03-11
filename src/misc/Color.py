from enum import Flag, auto


class Color(Flag):
    NONE = 0
    W = auto()
    U = auto()
    B = auto()
    R = auto()
    G = auto()
    C = auto()

    @classmethod
    def wrap(cls, color: str) -> str:
        return f"{{{color}}}"

    def as_mana(self) -> str:
        colors = str(self).split(".")[-1].split("|")
        return "|".join(self.wrap(c) for c in colors)

    def as_identity(self) -> str:
        colors = str(self).split(".")[-1].split("|")
        return "".join(self.wrap(c) for c in colors)
