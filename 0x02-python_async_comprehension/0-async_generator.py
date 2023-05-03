#!/usr/bin/env python3
"""
Async Generator
"""


import asyncio
import random


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Yields a number between 0 and 10
    """
    for i in range(10):
        yield random.uniform(0, 10)
        await asyncio.sleep(1)