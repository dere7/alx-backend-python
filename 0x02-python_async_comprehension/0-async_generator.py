#!/usr/bin/env python3
"""contains a function that loop 10x
each time async wait 1s, then yield rand num"""
import asyncio
from typing import Generator
import random


async def async_generator() -> Generator[float, None, None]:
    """loop 10x each time async wait 1s, then yield rand num"""
    for _ in range(10):
        await asyncio.sleep(1)
        rand = random.uniform(0, 10)
        yield rand
