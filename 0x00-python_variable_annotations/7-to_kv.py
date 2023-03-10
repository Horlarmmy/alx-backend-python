#!/usr/bin/env python3
""" Module 7-to_kv """

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ Function that joins to a tuple """

    return (k, v**2)
