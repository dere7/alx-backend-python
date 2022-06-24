#!/usr/bin/env python3
"""6-sum_mixed_list.py"""
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[float, int]]) -> float:
    """adds all items of list"""
    sum: float = 0
    for i in mxd_list:
        sum += i
    return sum
