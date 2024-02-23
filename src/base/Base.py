from abc import ABC
from dataclasses import dataclass
from datetime import date, datetime
from functools import cached_property, reduce
from operator import or_
from typing import Self, get_args
from uuid import UUID

from urllib3.util import Url, parse_url

from src.misc.Color import Color


@dataclass(frozen=True, kw_only=True)
class Base(ABC):
    @classmethod
    def from_dict(cls, data: dict) -> Self:
        return cls(**data)

    def __post_init__(self):
        for field in self.__dataclass_fields__.values():
            # get field type, can be anything similar to:
            #  - <class 'int'>
            #  - list[uuid.UUID]
            #  - dict[str, float]
            #  - typing.Optional[str]
            type_args = get_args(field.type)

            if not type_args:
                field_type = field.type
            elif type_args[-1] is type(None):
                field_type = type_args[-2]
            else:
                field_type = type_args[-1]

            # # check if field needs to be cast
            # if field_type not in self._types_to_cast:
            #    continue

            # retrieve field value and skip if it's null
            field_value = getattr(self, field.name)
            if field_value is None:
                continue

            # retrieve cast function for field type
            cast = self._types_to_cast.get(field_type, field_type)

            # cast to get the new field value
            if str(field.type).startswith("list"):
                new_value = [cast(value) for value in field_value]
            elif str(field.type).startswith("dict"):
                new_value = {key: cast(value) if value is not None else None for key, value in field_value.items()}
            else:
                new_value = cast(field_value)

            # assign new value to the field
            object.__setattr__(self, field.name, new_value)

    @cached_property
    def _types_to_cast(self):
        return {
            date: self._to_date,
            Color: self._to_color,
            Url: self._to_url,
            UUID: self._to_uuid,
        }

    def _to_date(self, value):
        return datetime.strptime(value, "%Y-%m-%d").date()

    def _to_color(self, value):
        return reduce(or_, [getattr(Color, c) for c in value], Color.NONE)

    def _to_url(self, value):
        return parse_url(value)

    def _to_uuid(self, value):
        return UUID(value)
