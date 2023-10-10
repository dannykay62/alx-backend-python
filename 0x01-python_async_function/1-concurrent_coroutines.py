#!/usr/bin/env python3
"""
    execute multiple coroutines at the same time with async
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
        return the list of all the delays (float values) without using sort()
    """
    c_routines = [waiit_random]