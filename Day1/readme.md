# Daily Programming Challenge - Day 1

## Problem Statement

You are given an array `arr` consisting only of `0`s, `1`s, and `2`s. The task is to sort the array in increasing order in linear time (i.e., O(n)) without using any extra space. This means you need to rearrange the array in-place.

### Example

- Input: `arr = [0, 1, 2, 1, 0, 2, 1, 0]`
- Output: `[0, 0, 0, 1, 1, 1, 2, 2]`

### Solution

The problem can be efficiently solved using the Dutch National Flag Algorithm (or 3-way partitioning). This algorithm maintains three pointers to place `0`s at the beginning, `2`s at the end, and `1`s in the middle in one pass.

### Implementations

- [Python Solution](Day1/Day1.py)

