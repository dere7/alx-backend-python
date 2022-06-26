#!/usr/bin/env python3
"""100-safe_first_element.py"""
from typing import Optional, Sequence, Any


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """gets first element if not empty"""
    if lst:
        return lst[0]
    else:
        return None
