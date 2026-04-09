"""Unit tests for dictionary utility functions."""

__author__ = "730765442"

import pytest
from exercises.ex05.dictionary import (
    invert,
    favorite_color,
    count,
    alphabetizer,
    update_attendance,
)


def test_invert_use_case_standard() -> None:
    """Test standard invert of unique keys and values."""
    assert invert({"a": "apple", "b": "banana"}) == {"apple": "a", "banana": "b"}


def test_invert_use_case_short() -> None:
    """Test invert of single character keys."""
    assert invert({"x": "y", "z": "w"}) == {"y": "x", "w": "z"}


def test_invert_edge_case_keyerror() -> None:
    """Test that duplicate values raise a KeyError."""
    with pytest.raises(KeyError):
        invert({"kris": "jordan", "michael": "jordan"})


def test_favorite_color_use_case_clear_winner() -> None:
    """Test finding the color with a clear majority."""
    assert favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}) == "blue"


def test_favorite_color_use_case_tie() -> None:
    """Test that a tie returns the color that appeared first."""
    assert favorite_color({"Marc": "yellow", "Ezri": "blue"}) == "yellow"


def test_favorite_color_edge_case_empty() -> None:
    """Test that an empty input returns an empty string."""
    assert favorite_color({}) == ""


def test_count_use_case_standard() -> None:
    """Test counting frequencies of a mixed list."""
    assert count(["a", "b", "a"]) == {"a": 2, "b": 1}


def test_count_use_case_unique() -> None:
    """Test counting a list where every item is unique."""
    assert count(["apple", "orange"]) == {"apple": 1, "orange": 1}


def test_count_edge_case_empty() -> None:
    """Test counting an empty list."""
    assert count([]) == {}


def test_alphabetizer_use_case_mixed_case() -> None:
    """Test grouping words while ignoring case."""
    assert alphabetizer(["Apple", "banana", "apple"]) == {
        "a": ["Apple", "apple"],
        "b": ["banana"],
    }


def test_alphabetizer_use_case_single_letter() -> None:
    """Test grouping single character strings."""
    assert alphabetizer(["a", "b", "c", "a"]) == {
        "a": ["a", "a"],
        "b": ["b"],
        "c": ["c"],
    }


def test_alphabetizer_edge_case_empty() -> None:
    """Test alphabetizing an empty list."""
    assert alphabetizer([]) == {}


def test_update_attendance_use_1() -> None:
    """Test adding student to new day."""
    attend: dict[str, list[str]] = {}
    update_attendance(attend, "Monday", "A")
    assert attend == {"Monday": ["A"]}


def test_update_attendance_use_2() -> None:
    """Test adding student to existing day."""
    attend: dict[str, list[str]] = {"Monday": ["A"]}
    update_attendance(attend, "Monday", "B")
    assert attend == {"Monday": ["A", "B"]}


def test_update_attendance_edge_case() -> None:
    """Test that duplicate names are not added."""
    attend: dict[str, list[str]] = {"Monday": ["A"]}
    update_attendance(attend, "Monday", "A")
    assert attend == {"Monday": ["A"]}
