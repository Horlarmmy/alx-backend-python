#!/usr/bin/env python3
""" Module 5-sum_list """


def sum_list(input_list: list[float]) -> float:
    """ Function that returns the sum of a list float """
    sum_i: float = 0
    for i in input_list:
        sum_i += i
    return sum_i
