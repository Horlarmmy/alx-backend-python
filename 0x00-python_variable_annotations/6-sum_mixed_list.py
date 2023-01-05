#!/usr/bin/env python3
""" Module 6-sum_mixed_list """

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ Function that returns the sum of a list float """
    sum_i: float = 0
    for i in mxd_lst:
        sum_i += i
    return sum_i
