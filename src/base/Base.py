from abc import ABC
from dataclasses import dataclass
from datetime import date, datetime
from enum import Flag
from functools import cached_property, reduce
from operator import or_
from typing import Self, get_args
from uuid import UUID

from urllib3.util import Url, parse_url


@dataclass(frozen=True, kw_only=True)
class Base(ABC):
    @classmethod
    def from_dict(cls, data: dict) -> Self:
        # params = inspect.signature(cls).parameters
        # return cls(**{k: v for k, v in data.items() if k in params})
        return cls(**data)

    def __post_init__(self):
        for field in self.__dataclass_fields__.values():
            field_type, iter_type = self._extract_type(field.type)

            # retrieve field value, skip field if it's None
            field_value = getattr(self, field.name)
            if field_value is None:
                continue

            # retrieve cast function for field type
            cast = self._types_to_cast.get(field_type, field_type)

            # TODO: add proper comment here
            if issubclass(cast, Base):
                cast = cast.from_dict

            # cast field value according to field type
            if issubclass(cast, Flag):
                new_value = reduce(or_, [getattr(cast, item) for item in field_value], 0)
            elif iter_type is list:
                new_value = [cast(value) for value in field_value]
            elif iter_type is dict:
                new_value = {key: cast(value) for key, value in field_value.items() if value is not None}
            else:
                new_value = cast(field_value)

            # assign new value to the field
            object.__setattr__(self, field.name, new_value)

    def _extract_type(self, field_type):
        # get field and iterator types; can be anything similar to:
        #  - <class 'int'>
        #  - list[uuid.UUID]
        #  - dict[str, float]
        #  - typing.Optional[str]

        # get the iterator type if it exists
        field_type_lower = str(field_type).lower()
        if "list[" in field_type_lower:
            iter_type = list
        elif "dict[" in field_type_lower:
            iter_type = dict
        else:
            iter_type = None

        # get the actual type of the field
        while any([field_type_lower.startswith(prefix) for prefix in ("typing.", "list[", "dict[")]):
            type_args = get_args(field_type)
            if not type_args:
                field_type = field_type
            elif type_args[-1] is type(None):
                field_type = type_args[-2]
            else:
                field_type = type_args[-1]

        return field_type, iter_type

    @cached_property
    def _types_to_cast(self):
        return {
            date: self._to_date,
            Url: self._to_url,
            UUID: self._to_uuid,
        }

    def _to_date(self, value):
        return datetime.strptime(value, "%Y-%m-%d").date()

    def _to_url(self, value):
        return parse_url(value)

    def _to_uuid(self, value):
        return UUID(value)
