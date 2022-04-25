"""Testing the implementation with some small input"""

from benchamarks.bm.knapsack_backtracking import knapsack_backtracking
from benchamarks.bm.knapsack_comm import Entry


def test_knapsack_backtracking_one() -> None:
    inputs = [
        Entry(60, 10),
        Entry(100, 20),
        Entry(120, 30),
    ]
    res = knapsack_backtracking(inputs, 50)
    assert res.max_val == 220
    assert res.elements == [30, 20]
