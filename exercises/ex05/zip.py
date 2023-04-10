""" Challenge Question 04 - Dict Function Writing."""
__author__ = 730621434

def zip(str_list: list[str], int_list: list[int]) -> dict[str, int]:
    """ Definition for the function to return the Dict."""
    if len(str_list) != len(int_list) or len(str_list) == [] or len(int_list) == []:
        return {}
    
    result: dict[str, int] = {}
    for i in range(len(str_list)):
        result[str_list[i]] = int_list[i]

    return result