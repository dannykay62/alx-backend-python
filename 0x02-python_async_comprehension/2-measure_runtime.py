#!/usr/bin/env python3
"""
    Import async_comprehension from the previous file and write
    a measure_runtime coroutine
"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
        execute async_comprehension four times in parallel using
        asyncio.gather and measure_runtime should measure the total
        runtime and return it.
    """
    begin = time.perf_counter()
    await asyncio.gather(*[async_comprehension() for _ in range(4)])
    finish = time.perf_counter()
    return finish - begin
