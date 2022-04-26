"""
Given weights and values of n items,
put these items in a knapsack of capacity W
to get the maximum total value in the knapsack

author: https://github.com/vincenzopalazzo
"""
from typing import Sequence

from .knapsack_comm import Entry


class Result:
    def __init__(self, max_val: int, elements: Sequence[int]):
        self.max_val = max_val
        self.elements = elements


def knapsack_backtracking(inputs: Sequence[Entry], capacity: int) -> Result:
    """
    Knapsack problem solved with a backtracking technique. in this solution, a list is returned too.

    :param inputs: the input of the problem.
    :param capacity: capacity of the knapsack.
    :return the maximum value calculated by the algorith.
    """
    table = [[0 for _ in range(capacity + 1)] for _ in range(len(inputs) + 1)]
    return knapsack_backtracking_helper(inputs, table, capacity)


def knapsack_backtracking_helper(
    inputs: Sequence[Entry], table: Sequence[Sequence[int]], capacity: int
) -> Result:
    """Helper function that helps to walt the table"""
    knapsack_dp_helper(inputs, table, capacity)
    max_cap = table[len(inputs)][capacity]
    elements = []
    max_cap_copy = max_cap
    for i in range(len(inputs) - 1, 0, -1):
        if max_cap_copy < 0:
            break

        if max_cap_copy == table[i - 1][capacity]:
            continue
        else:
            elements.append(inputs[i].weight)
            max_cap_copy -= inputs[i].value
            capacity -= inputs[i].weight

    return Result(max_cap, elements)


def knapsack_dp_helper(
    inputs: Sequence[Entry], table: Sequence[Sequence[int]], capacity: int
) -> None:
    """build the table where we will go do to backtracking. This table is built with a dynamic programming solution."""
    for i in range(len(inputs) + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                table[i][w] = 0
            elif inputs[i - 1].weight <= capacity:
                item = inputs[i - 1]
                take = item.value + table[i - 1][w - item.weight]
                untake = table[i - 1][w]
                table[i][w] = max(take, untake)
            else:
                table[i][w] = table[i - 1][w]
