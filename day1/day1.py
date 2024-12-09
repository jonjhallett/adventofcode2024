from collections import defaultdict
from typing import Tuple
from typing_extensions import Self
import unittest


def main() -> None:
    (list1, list2) = read_input("input.txt")
    print(total_distance(list1, list2))
    print(similarity_score(list1, list2))


def total_distance(list1: list[int], list2: list[int]) -> int:
    sorted_list1 = sorted(list1)
    sorted_list2 = sorted(list2)
    zipped_sorted_lists = zip(sorted_list1, sorted_list2)
    distances = [abs(distance1 - distance2)
                 for distance1, distance2 in zipped_sorted_lists]
    total_distance = sum(distances)
    return total_distance


def similarity_score(list1: list[int], list2: list[int]) -> int:
    list2_appearances = number_of_appearances(list2)
    weighted_scores = [i * list2_appearances[i] for i in list1]
    similarity_score = sum(weighted_scores)
    return similarity_score


def number_of_appearances(list_: list[int]) -> defaultdict[int, int]:
    number_of_appearances: defaultdict[int, int] = defaultdict(int)
    for i in list_:
        number_of_appearances[i] += 1
    return number_of_appearances


def read_input(filename: str) -> Tuple[list[int], list[int]]:
    list1 = []
    list2 = []

    with open(filename) as f:
        for line in f:
            split_line = line.split()
            list1.append(int(split_line[0]))
            list2.append(int(split_line[1]))

    return (list1, list2)


class TestDay1(unittest.TestCase):
    def test_total_distance(self: Self):
        fixture_str = """
            3   4
            4   3
            2   5
            1   3
            3   9
            3   3
            """
        list = fixture_str.split()
        list1 = map(int, list[0::2])
        list2 = map(int, list[1::2])
        self.assertEqual(total_distance(list1, list2), 11)

    def test_similarity_score(self: Self):
        fixture_str = """
            3   4
            4   3
            2   5
            1   3
            3   9
            3   3
            """
        fixture_list = fixture_str.split()
        list1 = list(map(int, fixture_list[0::2]))
        list2 = list(map(int, fixture_list[1::2]))

        self.assertEqual(similarity_score(list1, list2), 31)

    def test_number_of_appearances(self: Self):
        fixture = [1, 2, 3, 1, 1, 2]

        appearances = number_of_appearances(fixture)

        self.assertEqual(appearances[1], 3)
        self.assertEqual(appearances[2], 2)
        self.assertEqual(appearances[3], 1)
        self.assertEqual(appearances[4], 0)

    def test_read_input(self: Self):
        (list1, list2) = read_input("test.txt")

        self.assertListEqual(list1, [1, 2, 3, 4])
        self.assertListEqual(list2, [4, 3, 2, 1])



if __name__ == '__main__':
    main()
