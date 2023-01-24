#!/usr/bin/env python3
""" Module 8-make_multiplier.py """

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Function that retuns a callable function """
    return lambda x: x * multiplier
