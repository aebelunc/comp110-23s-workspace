"""EX05 - 'list' Utility Functions."""
__author__: 730621434


def only_evens(xs: list[int]) -> list[int]:
    """Function that only returns even integer values from a list."""
    even = []
    for item in xs:
        if item % 2 == 0:
            even.append(item)
    return even


def concat(list1: list[int], list2: list[int]) -> list[int]:
    """Function that returns in a new list all elements from both original lists."""
    new_list = []
    for element in list1:
        new_list.append(element)
    for element in list2:
        new_list.append(element)
    return new_list


def sub(list, start_idx, end_idx):
    """Function that returns a subset of the given list between the start and end."""
    if len(list) == 0 or start_idx >= len(list) or end_idx <= 0:
        return []
    if start_idx < 0:
        start_idx = 0
    if end_idx >= len(list):
        end_idx = len(list)
    subset = []
    for idx in range(start_idx, end_idx):
        subset.append(list[idx])
    return subset