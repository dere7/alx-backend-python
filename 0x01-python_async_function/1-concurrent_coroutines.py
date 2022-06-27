#!/usr/bin/env python3
"""1-concurrent_coroutines.py"""
import asyncio
wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n, max_delay):
    awaitables = [wait_random(max_delay) for _ in range(n)]
    return [await c for c in asyncio.as_completed(awaitables)]
