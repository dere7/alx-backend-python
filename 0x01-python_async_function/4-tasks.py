#!/usr/bin/env python3
"""4-tasks.py"""
import asyncio
task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n, max_delay):
    awaitables = [task_wait_random(max_delay) for _ in range(n)]
    return [await c for c in asyncio.as_completed(awaitables)]
