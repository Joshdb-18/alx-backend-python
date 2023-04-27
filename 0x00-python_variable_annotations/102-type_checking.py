#!/usr/bin/env python3
"""Validates function with mypy"""


from typing import List, Tuple


def zoom_array(lst: Tuple[int], factor: int = 2) -> Tuple[int]:
    """Codes"""
    zoomed_in: Tuple[int] = [
        item for item in lst
        for i in range(factor)
    ]
    return tuple(zoomed_in)


array: Tuple[int, int, int] = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
