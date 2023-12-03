import os

file_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "input.txt"
)
with open(file_path, 'r') as file:
    puzzle = file.read()


def is_int(char: str) -> bool:
    try:
        int(char)
        return True
    except ValueError:
        return False


value = 0

for line in puzzle.splitlines():
    ints = [char for char in line if is_int(char)]
    num = ints[0] + ints[-1]
    value += int(num)

print(value)  # 54561
