#!/usr/bin/env python3
""" Module 6-sum_mixed_list """


def sum_mixed_list(mxd_lst: list[float]) -> float:
    """ Function that returns the sum of a list float """
    sum_i: float = 0
    for i in mxd_lst:
        sum_i += i
    return sum_i
