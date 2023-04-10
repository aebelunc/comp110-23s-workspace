"""EX07 - Dictionary Functions Tests."""
__author__ = "730621434"


from exercises.ex07.dictionary import invert, favorite_color, count


def test_invert_case() -> None:
    """Test invert function with a empty dictionary."""
    assert invert({}) == {}


def test_invert_case1() -> None:
    """Test invert function for switching key and values."""
    assert invert({'a': 'z', 'b': 'y', 'c': 'x'}) == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_invert_case2() -> None:
    """Test invert function for switching key and values."""
    assert invert({'apple': 'cat'}) == {'cat': 'apple'}


def test_favorite_color_case() -> None:
    """Test favorite_color function with empty dictionary."""
    if favorite_color({}) is None:
        assert None


def test_favorite_color_case1() -> None:
    """Test favorite_color function with only one color."""
    assert favorite_color({"Austin": "blue"}) == "blue"


def test_favorite_color_case2() -> None:
    """Test favorite_color fuction with multiple colors."""
    assert favorite_color({"Jane": "red", "Julia": "blue", "Henry": "red", "Steve": "green", "Robert": "blue"}) == "red"


def test_count_case() -> None:
    """Test count function with an empty list."""
    assert count([]) == {}


def test_count_case1() -> None:
    """Test count function with only one key and value."""
    assert count(["b"]) == {"b": 1}


def test_count_case2() -> None:
    """Test count function with multiple values and keys."""
    assert count(["a", "b", "c", "c", "a", "a"]) == {"a": 3, "c": 2, "b": 1}