import re
from typing_extensions import Self
import unittest


def main() -> None:
    with open("input.txt") as file:
        corrupted_instructions = file.read()

    print(add_real_mul_instructions(corrupted_instructions))


def add_real_mul_instructions(corrupted_instructions: str) -> int:
    total_muls = 0

    all_muls = re.findall(r'mul\((\d+),(\d+)\)', corrupted_instructions)
    for arg1, arg2 in all_muls:
        total_muls += int(arg1) * int(arg2)

    return total_muls


class TestDay3(unittest.TestCase):
    def test_add_real_mul_instructions(self: Self) -> None:
        corrupted_instructions = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
        self.assertEqual(add_real_mul_instructions(corrupted_instructions),
                                                   161)

if __name__ == "__main__":
    main()
