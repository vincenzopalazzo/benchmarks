#! /usr/bin/python3
import random

import google_benchmark as benchmark

from benchamarks.bm.knapsack_greedy import Entry, knapsack_greedy
from benchamarks.bm.knapsack_dp import knapsack_dp


# TODO: there is some bug in the python porting of google benchmark?
@benchmark.register
#@benchmark.option.range(8, limit=8 << 10)
def bm_knapsack_greedy(state):
    #state.pause_timing()
    inputs = [
        Entry(random.randint(1, 400), random.randint(1, 400))
        for _ in range(900)
    ]
    #state.resume_timing()
    knapsack_greedy(inputs, random.randint(1, 400))


@benchmark.register
#@benchmark.option.range(8, limit=8 << 10)
def bm_knapsack_dp(state):
    #state.pause_timing()
    inputs = [
        Entry(random.randint(1, 400), random.randint(1, 400))
        for _ in range(900)
    ]
    #state.resume_timing()
    knapsack_dp(inputs, random.randint(2, 50))


if __name__ == "__main__":
    benchmark.main()
