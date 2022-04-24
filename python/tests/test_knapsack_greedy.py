"""Testing the implementation with some small input"""

from benchamarks.bm.knapsack_greedy import Entry, knapsack_greedy


def test_knapsack_greedy_one() -> None:
    inputs = [
        Entry(60, 10),
        Entry(40, 40),
        Entry(100, 20),
        Entry(120, 30),
    ]
    value = knapsack_greedy(inputs, 50)
    assert value == 240
