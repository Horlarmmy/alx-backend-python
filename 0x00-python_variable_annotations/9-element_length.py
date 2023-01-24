#!/usr/bin/env python3
""" Module 9-element_length """

from typing import List, Iterable, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Function that returns iterable of an element """
    return [(i, len(i)) for i in lst]
