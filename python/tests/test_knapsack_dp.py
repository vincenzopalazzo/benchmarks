"""Testing the implementation with some small input"""

from benchamarks.bm.knapsack_dp import knapsack_dp, Entry


def test_knapsack_dp_one() -> None:
    inputs = [
        Entry(60, 10),
        Entry(100, 20),
        Entry(120, 30),
    ]
    value = knapsack_dp(inputs, 50)
    assert value == 220
