#!/usr/bin/env python3
"""contains a function that executes async_comprehension 4x
in parallel"""
import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """executes async_comprehension 4x in parallel"""
    start_time = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.perf_counter() - start_time
