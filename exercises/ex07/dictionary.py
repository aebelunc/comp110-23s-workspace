"""EX07 - Dictionary Functions."""
__author__ = "730621434"


def invert(dict1: dict[str, str]) -> dict[str, str]:
    """Defintion for inverting key and values."""
    result: dict[str, str] = {}
    for key in dict1:
        if dict1[key] in result:
            raise KeyError
        value = dict1[key]
        result[value] = key
    return result


def favorite_color(colors: dict[str, str]) -> str:
    """Most frequent color is returned."""
    result: dict[str, int] = {}
    for key in colors:
        color = colors[key]
        if color in result:
            result[color] += 1
        else: 
            result[color] = 1
    full_count = 0
    favorite_color = None
    for key in colors:
        color = colors[key]
        count = result[color]
        if count > full_count or count == full_count and color == favorite_color:
            full_count = count 
            favorite_color = color 
    return favorite_color 


def count(list1: list[str]) -> dict[str, int]:
    """Defintion for counting unique values."""
    result: dict[str, int] = {}
    for value in list1:
        if value in result:
            result[value] += 1
        else:
            result[value] = 1
    return result