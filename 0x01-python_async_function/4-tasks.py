#!/usr/bin/env python3
"""contains a function that executes task_wait_random n times"""
import asyncio
from typing import List
task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """executes task_wait_random n times"""
    awaitables = [task_wait_random(max_delay) for _ in range(n)]
    return [await c for c in asyncio.as_completed(awaitables)]
