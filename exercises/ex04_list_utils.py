"""EX04 - List Utility Functions - append, list, pop, and len only."""

__author__ = "730765442"


def all(input_list: list[int], number: int) -> bool:
    if len(input_list) == 0:
        return False
    index: int = 0
    while index < len(input_list):
        if input_list[index] != number:
            return False
        index += 1
    return True


def max(input: list[int]) -> int:
    if len(input) == 0:
        raise ValueError("max()arg is an empty List")
    max_number: int = input[0]
    index: int = 1
    while index < len(input):
        if input[index] > max_number:
            max_number = input[index]
        index += 1
    return max_number


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    if len(list_1) != len(list_2):
        return False
    index: int = 0
    while index < len(list_1):
        if list_1[index] != list_2[index]:
            return False
        index += 1
    return True


def extend(first_list: list[int], second_list: list[int]) -> None:
    index: int = 0
    while index < len(second_list):
        first_list.append(second_list[index])
        index += 1
