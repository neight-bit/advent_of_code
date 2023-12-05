from src.aoc.aoc_helpers import get_input


def is_int(char: str) -> bool:
    try:
        int(char)
        return True
    except ValueError:
        return False


def is_num_word(string: str) -> (bool, int):
    nums = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        }
    for key, value in nums.items():
        if string.startswith(key):
            return (True, value)
    return (False, 0)


puzzle = get_input()

value = 0
for line in puzzle.splitlines():
    nums = []
    for i, char in enumerate(line):
        if is_int(char):
            nums.append(int(char))
        else:
            if char in ["o", "t", "f", "s", "e", "n"]:
                num_word = is_num_word(line[i:i+6])
                if num_word[0]:
                    nums.append(num_word[1])

    num = str(nums[0]) + str(nums[-1])
    value += int(num)

print(value)  # 54076
