"""EX05 - Utils Tests."""
__author__ = 730621434

from exercises.ex05.utils import only_evens, sub, concat


def test_even1() -> None:
    """Tests the only_evens function for correctness."""
    test_even1: list[int] = [1, 2, 3]
    assert only_evens(test_even1) == [2]


def test_even2() -> None:
    """Tests the only_evens function for correctness."""
    test_even2: list[int] = [1, 5, 3]
    assert only_evens(test_even2) == []


def test_even3() -> None:
    """Tests the only_evens function for correctness."""
    test_even3: list[int] = [4, 4, 4]
    assert only_evens(test_even3) == [4, 4, 4]


def test_concat1() -> None:
    """Tests the concat function for correctness."""
    test_concat: list[int] = [1, 2, 4]
    test_concat2: list[int] = [3, 6, 9]
    assert concat(test_concat, test_concat2) == [1, 2, 4, 3, 6, 9]


def test_concat2() -> None:
    """Tests the concat function for correctness."""
    test_concat: list[int] = [1, 3, 5]
    test_concat2: list[int] = [3, 7, 8]
    assert concat(test_concat, test_concat2) == [1, 3, 5, 3, 7, 8]


def test_concat3() -> None:
    """Tests the concat function for correctness."""
    test_concat: list[int] = [2, 2, 5]
    test_concat2: list[int] = [4, 6, 9]
    assert concat(test_concat, test_concat2) == [2, 2, 5, 4, 6, 9]


def test_sub1() -> None:
    """Tests the sub function for correctness."""
    test_sub1: list[int] = [10, 20, 30, 40]
    assert sub(test_sub1, 1, 3) == [20, 30]


def test_sub2() -> None:
    """Tests the sub function for correctness."""
    test_sub2: list[int] = [11, 20, 40, 50]
    assert sub(test_sub2, 1, 3) == [20, 40]


def test_sub3() -> None:
    """Tests the sub function for correctness."""
    test_sub3: list[int] = [10, 15, 25, 35, 50]
    assert sub(test_sub3, 1, 3) == [15, 25]