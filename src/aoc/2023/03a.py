from src.aoc.aoc_helpers import get_input
from rich import print

puzzle_input: str = get_input()


class Cell():
    
    def __init__(self, x, y):
        self.starting_x = x
        self.starting_y = y
        self.ending_x = None
        self.number = None
        
    def get_number(self):
        if not self.number:
            self.number = []
            position = [self.starting_x, self.starting_y]
            while get_char(*position).isdigit():
                self.number.append(get_char(*position))
                position[0] += 1
            self.number = int(''.join(map(str, self.number)))
            self.ending_x = self.starting_x + len(str(self.number))
        print(f'cell number: {self.number}')
        print(f'cell number position: {self.starting_x}-{self.ending_x-1}, {self.starting_y}')
        return self.number


rows = [row for row in puzzle_input.splitlines()]
columns = ["".join(column) for column in zip(*rows)]

def get_char(x,y) -> str:
    return rows[y-1][x-1]

for row_num, row in enumerate(rows, start=1):
    position = [1, 1]
    for char in row:
        char = get_char(*position)
        if char.isdigit():
            cell = Cell(*position)
            number = cell.get_number()
            position[0] = (cell.ending_x)
        else:
            position[0] += 1




