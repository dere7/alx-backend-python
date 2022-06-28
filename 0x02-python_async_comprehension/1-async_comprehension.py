#!/usr/bin/env python3
"""contains a function that collect 10 rand nums
using async comprehension"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """collect 10 rand nums using async comprehension"""
    return [i async for i in async_generator()]
