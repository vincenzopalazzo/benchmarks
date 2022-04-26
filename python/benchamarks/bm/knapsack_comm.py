"""
Comm module contains all the information to deal with
the datatype in the knapsack module.

author: https://github.com/vincenzopalazzo
"""


class Entry:
    """Wrapping around the input of th problem,
    just to keep the code more readable"""

    def __init__(self, value: int, weight: int):
        self.value = value
        self.weight = weight

    def ratio(self) -> int:
        """This is the core of the fractional knapsack problem
        solution"""
        return self.value // self.weight

    def __lt__(self, other):
        return self.ratio() < other.ratio()
