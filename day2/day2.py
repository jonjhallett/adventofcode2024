from itertools import combinations
from typing_extensions import Self
import unittest


def main() -> None:
    list_of_levels = read_list_of_levels("input.txt")

    number_of_safe_levels = 0
    for levels in list_of_levels:
        if is_safe(levels):
            number_of_safe_levels += 1

    print(number_of_safe_levels)

    number_of_dampened_safe_levels = 0
    for levels in list_of_levels:
        if is_safe_with_dampening(levels):
            number_of_dampened_safe_levels += 1

    print(number_of_dampened_safe_levels)


def level_deltas(levels: list[int]) -> list[int]:
    deltas = []

    previous_level = levels[0]
    for level in levels[1:]:
        delta = level - previous_level
        previous_level = level
        deltas.append(delta)

    return deltas


def is_safe(levels: list[int]) -> bool:
    deltas = level_deltas(levels)

    if all([1<= delta <= 3 for delta in deltas]):
        return True
    if all([-3 <= delta <= -1 for delta in deltas]):
        return True
    return False 


def is_safe_with_dampening(levels: list[int]) -> bool:
    number_of_levels = len(levels)
    list_of_dampened_levels = combinations(levels, number_of_levels - 1)
    for dampened_levels in list_of_dampened_levels:
        if is_safe(dampened_levels):
            return True
    return False


def read_list_of_levels(filename: str) -> list[list[int]]:
    list_of_levels = []

    with open(filename) as f:
        for line in f:
            levels = list(map(int, line.split()))
            list_of_levels.append(levels)

    return list_of_levels


class TestIsSafe(unittest.TestCase):
    def test_is_safe(self: Self) -> None:
        self.assertTrue(is_safe([7, 6, 4, 2, 1]))
        self.assertFalse(is_safe([1, 2, 7, 8, 9]))
        self.assertFalse(is_safe([9, 7, 6, 2, 1]))
        self.assertFalse(is_safe([1, 3, 2, 4, 5]))
        self.assertFalse(is_safe([8, 6, 4, 4, 1]))
        self.assertTrue(is_safe([1, 3, 6, 7, 9]))

    def test_deltas(self: Self) -> None:
        self.assertListEqual(level_deltas([7, 6, 4, 2, 1]), [-1, -2, -2, -1])
        self.assertListEqual(level_deltas([1, 2, 7, 8, 9]), [1, 5, 1, 1])

    def test_is_safe_with_dampening(self: Self) -> None:
        self.assertTrue(is_safe_with_dampening([7, 6, 4, 2, 1]))
        self.assertFalse(is_safe_with_dampening([1, 2, 7, 8, 9]))
        self.assertFalse(is_safe_with_dampening([9, 7, 6, 2, 1]))
        self.assertTrue(is_safe_with_dampening([1, 3, 2, 4, 5]))
        self.assertTrue(is_safe_with_dampening([8, 6, 4, 4, 1]))
        self.assertTrue(is_safe_with_dampening([1, 3, 6, 7, 9]))

    def test_read_list_of_levels(self: Self) -> None:
        list_of_levels = read_list_of_levels("test.txt")
        self.assertListEqual(list_of_levels[0], [7, 6, 4, 2, 1])
        self.assertListEqual(list_of_levels[5], [1, 3, 6, 7, 9])


if __name__ == "__main__":
    main()

