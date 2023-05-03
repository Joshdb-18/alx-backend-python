#!/usr/bin/env python3
"""
Task 2
"""


import asyncio
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Returns 10 random numbers
    """
    return [x async for x in async_generator()]
