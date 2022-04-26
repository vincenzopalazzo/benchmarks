"""
Given weights and values of n items, we need to put these items in a knapsack of
capacity W to get the maximum total value in the knapsack.

The greedy solution here is no possible with a standard 0/1 knapsack problem,
so, we implement an alternative to the algorithm.

author: https://github.com/vincenzopalazzo
"""
from typing import Sequence
from .knapsack_comm import Entry


def knapsack_greedy(inputs: Sequence[Entry], capacity: int) -> int:
    """Implementing the solution to knapsack problem with
    a greedy approach.

    idea: The basic idea of the greedy approach is to calculate the ratio value/weight
    for each item and sort the item on the basis of this ratio. Then take the item with the
    highest ratio and add them until we can’t add the next item as a whole and at the end
    add the next item as much as we can.
    Which will always be the optimal solution to this problem.

    :param inputs: The input of the problem
    :param capacity: The maximum capacity of the knapsack.
    :return the maximum value that it is possible to obtain
    """

    # core of the greedy approach
    # we sort the element in the reverse order by
    # ratio.
    inputs.sort(reverse=True)

    tot_value = 0
    for _, input in enumerate(inputs):

        if capacity - input.weight >= 0:
            # count the knapsack is there is space
            capacity -= input.weight
            tot_value += input.value
        else:
            # we are in sorted order, so we insert
            # to remain capacity, and we exit the loop
            fraction = capacity / input.weight
            tot_value += input.value * fraction
            capacity = int(capacity - (input.weight * fraction))
            break
    return tot_value
