#!/usr/bin/env python3
"""
    measures the total execution time for 
"""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measur_time(n: int, max_delay: int) -> float:
    """
        measures the total execution time for wait_n(n, max_delay),
        and returns total_time / n
    """
    beegin = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    finish = time.perf_counter()
    return (finish - beegin) / n
