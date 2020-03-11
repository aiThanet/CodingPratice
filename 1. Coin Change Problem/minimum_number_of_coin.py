#!/bin/python3

import math
import os
import random
import re
import sys


def main(total, coins):

    _min = [float('inf') for _ in range(total+1)]
    _min[0] = 0
    _min_list = [[] for _ in range(total+1)]

    # solution1
    for s in range(1, total+1):
        for i in range(len(coins)):
            if(s-coins[i] >= 0 and coins[i] <= s and _min[s] > _min[s-coins[i]] + 1):
                _min[s] = _min[s-coins[i]] + 1
                # Which coins use
                _min_list[s] = _min_list[s-coins[i]].copy()
                _min_list[s].append(coins[i])

    # solution2
    # for s in range(0, total+1):
    #     for i in range(len(coins)):
    #         if(s+coins[i] <= total and _min[s+coins[i]] > _min[s] + 1):
    #             _min[s+coins[i]] = _min[s] + 1

    print(-1 if _min[total] == float('inf') else _min[total])
    print(_min_list[total])


if __name__ == '__main__':
    total = int(sys.argv[1].strip())
    coins = list(map(int, sys.argv[2].rstrip().split()))
    main(total, coins)
