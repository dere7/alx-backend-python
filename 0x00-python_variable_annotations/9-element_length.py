#!/usr/bin/env python3
"""9-element_length.py"""
from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """gets list of pair of item and its length"""
    return [(i, len(i)) for i in lst]
