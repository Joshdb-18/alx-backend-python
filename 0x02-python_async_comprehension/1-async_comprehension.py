#!/usr/bin/env python3
"""
Async Comprehension
"""


from typing import List
from importlib import import_module as scan


async_generator = scan('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Returns 10 random numbers
    """
    return [x async for x in async_generator()]

