"""Testing the implementation with some small input"""

from benchamarks.bm.knapsack_branching import knapsack_branching
from benchamarks.bm.knapsack_comm import Entry


def test_knapsack_branching_one() -> None:
    inputs = [
        Entry(40, 2),
        Entry(50, 3.14),
        Entry(100, 1.98),
        Entry(95, 5),
        Entry(30, 3),
    ]
    res = knapsack_branching(inputs, 10)
    assert res == 235
