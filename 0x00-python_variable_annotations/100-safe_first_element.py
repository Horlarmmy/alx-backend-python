#!/usr/bin/env python3
""" Module 100-safe_first_element.py"""

from typing import Union, Sequence, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ Function that returns the first element """
    if lst:
        return lst[0]
    else:
        return None
