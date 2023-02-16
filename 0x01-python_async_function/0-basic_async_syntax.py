#!/usr/bin/env python3
""" Module - 0-basic_async_syntax """

import asyncio
import random


async def wait_random(max_delay=10):
    delay = random.triangular(0, max_delay)
    await asyncio.sleep(delay)
    return delay
