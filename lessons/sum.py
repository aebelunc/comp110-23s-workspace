"""Example function for unit tests."""

def sum(xs: list[float]) -> float:
    """return sum off all elements in xs"""
    item = 0
    for idx in range(len(xs)):       
        item += xs[idx]
    return item