#!/usr/bin/env python3
""" Module 2-measure_runtime"""

import asyncio
import random
import time
from typing import List
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ Function that returns average time taken"""
    begin = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    total_time = end - begin
    return (total_time/n)
