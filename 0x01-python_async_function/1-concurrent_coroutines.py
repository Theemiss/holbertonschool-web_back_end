#!/usr/bin/env python3
""" 1. Let's execute multiple coroutines at the same time with async"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n, max_delay):
    """
    """
    tasks = []
    for i in range(n):
        tasks.append(wait_random(max_delay))
    return [await task for task in asyncio.as_completed(tasks)]
