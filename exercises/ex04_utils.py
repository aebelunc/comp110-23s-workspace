"""EX04 - 'list' Utility Functions."""
__author__ = 730621434


def all(lists: list[int], indicated_num: int) -> bool:
    """All function checks for similar values in seperate between list and int."""
    if len(lists) == 0:
        return False
    idx = 0
    while idx < len(lists):
        if lists[idx] == indicated_num:
            idx += 1
        else:
            return False
    return True


def max(input: list[int]) -> int:
    """Max function returns largest value in the list."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    max_idx = input[0]
    current_max = 0
    idx = 1
    while idx < len(input):
        if input[idx] > max_idx:
            max_idx = input[idx]
            current_max = max_idx
            idx += 1
        else:
            if input[idx] < max_idx:
                current_max = max_idx
            idx += 1
    return current_max


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """is_equal function checks the indices to make sure they are equal."""
    if len(list1) != len(list2):
        return False
    idx = 0
    while idx < len(list1) and idx < len(list2):
        if list1[idx] == list2[idx]:
            idx += 1
        else:
            if list1[idx] != list2[idx]:
                return False
    return True
