#!/usr/bin/env python3

import random
import time

def binary_search_rec(arr, key):
    def __binary_search_rec(arr, low, high, key):
        if high >= low:
            mid = (high + low) // 2
            if arr[mid] == key:
                return mid
            elif arr[mid] > key:
                return __binary_search_rec(arr, low, mid - 1, key)
            else:
                return __binary_search_rec(arr, mid + 1, high, key)
        else:
            return -1
    return __binary_search_rec(arr, 0, len(arr) - 1, key)

def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

def binary_search(arr, key):
    pass

def interpolation_search(arr, key):
    pass


arr = [random.randint(0, 10000000) for i in range(1000000)]
arr.sort()
keys = [arr[random.randint(0, 1000000)] for i in range(10)]
keys.extend(random.randint(0, 1000000)  for i in range(5))

# TODO: benchmark linear search, binary search, and interpolation search for the given keys
start = time.perf_counter_ns()
found = linear_search(arr, keys[0])
end = time.perf_counter_ns()
