from src.aoc.aoc_helpers import get_input


def is_int(char: str) -> bool:
    try:
        int(char)
        return True
    except ValueError:
        return False

puzzle = get_input()

value = 0
for line in puzzle.splitlines():
    ints = [char for char in line if is_int(char)]
    num = ints[0] + ints[-1]
    value += int(num)

print(value)  # 54561
