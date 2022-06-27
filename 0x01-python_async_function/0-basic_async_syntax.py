#!/usr/bin/env python3
"""contains a function that waits for random delay"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """waits for random delay"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
