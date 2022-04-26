"""
Given weights and values of n items,
put these items in a knapsack of capacity W
to get the maximum total value in the knapsack

author: https://github.com/vincenzopalazzo
"""
import functools
import logging
import queue
from typing import Sequence
from benchamarks.bm.knapsack_comm import Entry


class Node:
    def __init__(self, level: int, profit: int, bound: int, weight: float):
        self.level = level
        self.profit = profit
        self.bound = bound
        self.weight = weight

    def compute_bound(self, inputs: Sequence[Entry], capacity: int) -> None:
        """Find the upper bound on the maximum profit in the subtree rooted to this node.

        :param inputs: the input sequence of the values
        :param capacity: the capacity of the knapsack.
        :return the local maximum profit calculated in the subtree.
        """
        if self.weight >= capacity:
            return 0
        profit_bound = self.profit
        next_level = self.level + 1
        tot_weight = self.weight

        while (next_level < len(inputs)) and (
            tot_weight + inputs[next_level].weight <= capacity
        ):
            tot_weight += inputs[next_level].weight
            profit_bound += inputs[next_level].value
            next_level += 1

        if next_level < len(inputs):
            # if we exit before without reach the leaf of the tree
            # we include the last item partially
            profit_bound += (capacity - tot_weight) * (
                inputs[next_level].value / inputs[next_level].weight
            )

        self.bound = profit_bound


def cmp_items(a: Entry, b: Entry) -> int:
    """Compare to entry items"""
    r1 = a.value / a.weight
    r2 = b.value / b.weight
    if r1 > r2:
        return 1
    elif r1 < r2:
        return -1
    return 0


def knapsack_branching(inputs: Sequence[Entry], capacity: int) -> int:
    """Knapsack solution solved with a more advanced technology of algorithm design.

    The technique used is branching, Branch and bound is an algorithm design paradigm which is generally used for solving
    combinatorial optimization problems. These problems are typically exponential in terms of time complexity and may require
    exploring all possible permutations in the worst case.

    Branch and Bound solve these problems relatively quickly.

    Solution steps:
    1. Sort all items in decreasing order of ratio of value per unit weight so that an upper bound can be computed using Greedy Approach.
    2. Initialize maximum profit, maxProfit = 0
    3. Create an empty queue, Q.
    4. Create a dummy node of decision tree and enqueue it to Q. Profit and weight of dummy node are 0.
    5. Do following while Q is not empty.
       5.1 Extract an item from Q. Let the extracted item be u.
       5.2 Compute profit of next level node. If the profit is more than maxProfit, then update maxProfit.
       5.3 Compute bound of next level node. If bound is more than maxProfit, then add next level node to Q.
       5.4 Consider the case when next level node is not considered as part of solution and add a node to queue with level as next,
           but weight and profit without considering next level nodes.

    :param inputs: the input of the problem.
    :param capacity: capacity of the knapsack.
    :return the maximum value calculated by the algorith.
    """
    inputs.sort(key=functools.cmp_to_key(cmp_items))
    queue_nodes = queue.Queue()

    node_u = Node(level=-1, profit=0, bound=0, weight=0.0)
    node_v = Node(level=-1, profit=0, bound=0, weight=0.0)
    queue_nodes.put(node_u)

    max_profit = 0

    while not queue_nodes.empty():
        node_u = queue_nodes.get()
        if node_u.level == -1:
            node_v.level = 0

        if node_u.level == len(inputs) - 1:
            continue

        node_v.level += 1
        item = inputs[node_v.level]
        node_v.weight = node_u.weight + item.weight
        node_v.profit = node_u.profit + item.value

        if node_v.weight <= capacity and node_v.profit > max_profit:
            max_profit = node_v.profit

        node_v.compute_bound(inputs, capacity)

        if node_v.bound > max_profit:
            queue_nodes.put(node_v)

        node_v.weight = node_u.weight
        node_v.profit = node_u.profit
        node_v.compute_bound(inputs, capacity)
        if node_v.bound > max_profit:
            queue_nodes.put(node_v)

    return max_profit
