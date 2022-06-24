#!/usr/bin/env python3
"""8-make_multiplier.py"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """gets multiplier function"""
    return lambda x: multiplier * x
