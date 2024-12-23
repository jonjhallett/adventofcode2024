import unittest
from typing import Tuple
from typing_extensions import Iterable, Self


def main() -> None:
    with open("input.txt") as file:
      puzzle_string = file.read()

    puzzle = Puzzle(puzzle_string.split())
    instances_of_xmas = puzzle.instances_found("XMAS")
    print(instances_of_xmas)


class Puzzle:
    def __init__(self: Self, puzzle: Iterable[str]):
        self.rows: list[str] = []
        for row in puzzle:
            self.rows.append(row)

    def __getitem__(self: Self, position: Tuple[int, int]) -> str:
        column, row = position
        return self.rows[row][column]

    def instances_found(self: Self, word: str) -> int:
        count = 0
        for j in range(0, len(self.rows)):
            for i in range(0, len(self.rows[0])):
                count += self.instances_at_position(word, i, j)
        return count

    def instances_at_position(self: Self, word: str,
                              column: int, row: int) -> int:

        count = 0
        for delta_j in range(-1, 2):
            for delta_i in range(-1, 2):
                if delta_i == delta_j == 0:
                    next
                if self.instance_in_direction(word,
                                              column, row,
                                              delta_i, delta_j):
                    count += 1
        return count

    def instance_in_direction(self: Self, word: str,
                              column: int, row: int,
                              delta_i, delta_j) -> bool:
        while True:
            if not 0 <= column < len(self.rows[0]):
                return False
            if not 0 <= row < len(self.rows):
                return False

            if self.rows[row][column] != word[0]:
                return False

            rest_of_word = word[1:]
            if rest_of_word == "":
                return True

            word = rest_of_word
            column += delta_i
            row += delta_j


class TestDay4(unittest.TestCase):
    fixture_string = """
        ..X...
        .SAMX.
        .A..A.
        XMAS.S
        .X....
        """
    fixture_iterable = fixture_string.split()

    def test_load_puzzle(self: Self) -> None:
        puzzle = Puzzle(TestDay4.fixture_iterable)
        self.assertEqual(puzzle[2, 0], 'X')
        self.assertEqual(puzzle[3, 1], 'M')
        self.assertEqual(puzzle[1, 4], 'X')

    def test_instances_found(self: Self) -> None:
        puzzle = Puzzle(TestDay4.fixture_iterable)
        instances_of_xmas = puzzle.instances_found("XMAS")
        self.assertEqual(instances_of_xmas, 4)

    def test_instance_at_position(self: Self) -> None:
        puzzle = Puzzle(TestDay4.fixture_iterable)
        self.assertEqual(puzzle.instances_at_position("XMAS", -1, 0), 0)
        self.assertEqual(puzzle.instances_at_position("XMAS", 6, 0), 0)
        self.assertEqual(puzzle.instances_at_position("XMAS", 0, -1), 0)
        self.assertEqual(puzzle.instances_at_position("XMAS", 0, 5), 0)
        self.assertEqual(puzzle.instances_at_position("XMAS", 0, 0), 0)
        self.assertEqual(puzzle.instances_at_position("XMAS", 5, 0), 0)
        self.assertEqual(puzzle.instances_at_position("XMAS", 0, 3), 1)
        self.assertEqual(puzzle.instances_at_position("XMAS", 2, 0), 1)

    def test_instances_found_complex(self: Self) -> None:
        complex_fixture_string = """
        MMMSXXMASM
        MSAMXMSMSA
        AMXSXMAAMM
        MSAMASMSMX
        XMASAMXAMM
        XXAMMXXAMA
        SMSMSASXSS
        SAXAMASAAA
        MAMMMXMMMM
        MXMXAXMASX
        """
        complex_fixture_iterable = complex_fixture_string.split()
        puzzle = Puzzle(complex_fixture_iterable)
        instances_of_xmas = puzzle.instances_found("XMAS")
        self.assertEqual(instances_of_xmas, 18)


if __name__ == '__main__':
    main()
