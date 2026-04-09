"""Ex05 - Dictionary Utility Functions."""

__author__: str = "730765442"


def invert(input: dict[str, str]) -> dict[str, str]:
    """Swap values with key."""
    result: dict[str, str] = {}

    for key in input:
        value: str = input[key]

        if value in result:
            raise KeyError("Duplicates cant be inverted.")
        result[value] = key
    return result


def favorite_color(fav: dict[str, str]) -> str:
    """Count up colors associated with person."""
    color_counts: dict[str, int] = {}
    for person in fav:
        color: str = fav[person]
        if color in color_counts:
            color_counts[color] += 1
        else:
            color_counts[color] = 1
    most_popular: str = ""
    max_count: int = 0

    for color in color_counts:
        if color_counts[color] > max_count:
            max_count = color_counts[color]
            most_popular = color
    return most_popular


def count(values: list[str]) -> dict[str, int]:
    """Count of the number of times that value appeared in the input list."""
    result: dict[str, int] = {}
    for item in values:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    """Group words by first letter."""
    result: dict[str, list[str]] = {}

    for word in words:
        letter: str = word[0].lower()
        if letter.isalpha():
            if letter in result:
                result[letter].append(word)
            else:
                result[letter] = [word]

    return result


def update_attendance(attendance: dict[str, list[str]], day: str, student: str) -> None:
    """Update attendance without adding duplicate names to the same day."""
    if day in attendance:
        if student not in attendance[day]:
            attendance[day].append(student)
    else:
        attendance[day] = [student]
