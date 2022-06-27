#!/usr/bin/env python3
"""contains a function that  executes wait_random n times and waits for them"""
import asyncio
from typing import List
wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """executes wait_random n times and waits for them"""
    awaitables = [wait_random(max_delay) for _ in range(n)]
    return [await c for c in asyncio.as_completed(awaitables)]
