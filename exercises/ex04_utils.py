"""Become familiar with the names and behaviors of commonly useful functions."""
__author__ = "730571588"


def all(ints: list[int], num: int) -> bool:
    """Return a bool indicating whether or not all the ints in the list are the same as the given int."""
    if len(ints) == 0:
        return False
    idx = 0
    while idx < len(ints):
        if num != ints[idx]:
            return False
        idx += 1
    return True 


def max(ints: list[int]) -> int:
    """Return the largest in the List."""
    if len(ints) == 0:
        raise ValueError("max() arg is an empty list.")
    idx = 0
    tracker: int = ints[idx]
    while idx < len(ints):
        if tracker < ints[idx]:
            tracker = ints[idx]
        idx += 1
    return tracker


def is_equal(ints: list[int], nums: list[int]) -> bool:
    """Return bool indicating if every element at even index is equal in both lists."""
    if len(ints) != len(nums):
        return False
    idx = 0
    while idx < len(ints):
        if ints[idx] != nums[idx]:
            return False 
        idx += 1
    return True