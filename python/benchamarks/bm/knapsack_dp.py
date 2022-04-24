"""
Given weights and values of n items,
put these items in a knapsack of capacity W
to get the maximum total value in the knapsack

author: https://github.com/vincenzopalazzo
"""
from typing import Sequence


class Entry:
    def __init__(self, value: int, weight: int):
        self.value = value
        self.weight = weight


def knapsack_dp(inputs: Sequence[Entry], capacity: int) -> int:
    """Knapsack problem resolved with dynamic programming implementation
    with a specie optimization implementation.

    :param inputs: the input of the problem
    :return the maximum capacity calculated from the import
    """
    table = [[-1 for _ in range(capacity + 1)] for _ in range(len(inputs) + 1)]
    return knapsack_dp_helper(inputs, table, capacity, len(inputs))


def knapsack_dp_helper(
    inputs: Sequence[Entry],
    table: Sequence[Sequence[int]],
    capacity: int,
    element_size: int,
) -> int:
    """Helper function to apply the knapsack optimized solution"""
    if capacity == 0 or element_size == 0:
        return 0

    if table[element_size][capacity] != -1:
        # We have already calculated this, so we can just return it
        return table[element_size][capacity]

    item = inputs[element_size - 1]
    if item.weight <= capacity:
        take = item.value + knapsack_dp_helper(
            inputs, table, capacity - item.weight, element_size - 1
        )
        untake = knapsack_dp_helper(inputs, table, capacity, element_size - 1)
        table[element_size][capacity] = max(take, untake)
        return table[element_size][capacity]
    elif item.weight > capacity:
        table[element_size][capacity] = knapsack_dp_helper(
            inputs, table, capacity, element_size - 1
        )
        return table[element_size][capacity]
