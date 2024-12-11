import re
from typing_extensions import Self
import unittest


def main() -> None:
    with open("input.txt") as file:
        corrupted_instructions = file.read()

    print(add_mul_instructions(corrupted_instructions))
    corrupted_instructions_with_donts_removed = remove_donts(corrupted_instructions)
    print(add_mul_instructions_in_dos(corrupted_instructions))


def add_mul_instructions(corrupted_instructions: str) -> int:
    total_muls = 0

    all_muls = re.findall(r'mul\((\d+),(\d+)\)', corrupted_instructions)
    for arg1, arg2 in all_muls:
        total_muls += int(arg1) * int(arg2)

    return total_muls


def remove_donts(corrupted_instructions: str) -> str:
    return re.sub(r'don\'t\(\).*?(do\(\)|\Z)', '',
                  corrupted_instructions, flags=re.MULTILINE | re.DOTALL)


def add_mul_instructions_in_dos(corrupted_instructions: str) -> int:
    instructions_with_donts_removed = remove_donts(corrupted_instructions)
    return add_mul_instructions(instructions_with_donts_removed)


class TestDay3(unittest.TestCase):
    def test_add_mul_instructions(self: Self) -> None:
        corrupted_instructions = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
        self.assertEqual(add_mul_instructions(corrupted_instructions),
                                                   161)
    def test_remove_donts(self: Self) -> None:
        dont_fixture = """xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+
mul(32,64](mul(11,8)undo()?mul(8,5))"""
        self.assertEqual(remove_donts(dont_fixture),
                         "xmul(2,4)&mul[3,7]!^?mul(8,5))")

        dont_at_end_fixture = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)un?mul(8,5))"
        self.assertEqual(remove_donts(dont_at_end_fixture),
                         "xmul(2,4)&mul[3,7]!^")

    def test_add_mul_instructions_in_dos(self: Self) -> None:
        corrupted_instructions = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
        self.assertEqual(add_mul_instructions_in_dos(corrupted_instructions),
                         48)


if __name__ == "__main__":
    main()
