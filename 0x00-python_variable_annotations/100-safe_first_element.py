#!/usr/bin/env python3
"""100-safe_first_element.py"""
from typing import Sequence, Any, Union
from types import NoneType


def safe_first_element(lst: Sequence[Any]) -> Union[Any, NoneType]:
    """gets first element if not empty"""
    if lst:
        return lst[0]
    else:
        return None
