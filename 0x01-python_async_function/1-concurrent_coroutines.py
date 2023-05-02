#!/usr/bin/env python3
"""
Multiplies coroutines at the same time with async
"""


import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Multiple coroutines: returns the list of all the delays
    (float values) in ascending order without using sort()
    """
    delays = [wait_random(max_delay) for i in range(n)]
    completed = await asyncio.gather(*delays)
    return sorted(completed)
