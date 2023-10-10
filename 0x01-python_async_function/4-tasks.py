#!/usr/bin/env python3
"""
    calls task_wait_random
"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
        Take the code from wait_n and alter it into a new function task_wait_n
    """
    routines = [task_wait_random(max_delay) for _ in range(n)]
    return [await delay for delay in asyncio.as_completed(routines)]
