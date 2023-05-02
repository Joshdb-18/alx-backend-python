#!/usr/bin/env python3
"""
Tasks
"""


import asyncio
from typing import List
from random import uniform


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Multiple coroutines: returns the list of all the delays
    (float values) in ascending order.
    """
    tasks = [task_wait_random(max_delay) for i in range(n)]
    completed = []
    for task in asyncio.as_completed(tasks):
        result = await task
        completed.append(result)
    return completed
