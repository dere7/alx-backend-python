#!/usr/bin/env python3
"""101-safely_get_value.py"""
from typing import Any, Union, Mapping, TypeVar
from types import NoneType

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, NoneType] = None
                     ) -> Union[Any, T]:
    """gets first element if not empty"""
    if key in dct:
        return dct[key]
    else:
        return default