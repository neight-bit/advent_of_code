from src.aoc.aoc_helpers import get_input
from rich import print

puzzle_input: str = get_input()

games = {}

# Iterate through the input data
for game_number in puzzle_input.splitlines():
    
    highest_count_per_game = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }

    # Process the text into data structures
    dict_items = game_number.split(':')
    game_number = int(dict_items[0].split(" ")[1])
    cube_samples = dict_items[1].split(";")
    
    for sample in cube_samples:
        # More processing
        results = sample.split(",")
        for result in results:
            result = result.lstrip().split(" ")
            qty = int(result[0])
            color = result[1]

            # Compare the sample against the indexed highest count for each color
            if qty > highest_count_per_game[color]:
                 highest_count_per_game[color] = qty

    games[game_number] = highest_count_per_game

# Now that we have the highest number of each color cube for each game, compare it the cube limit
cube_limit = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

possible_games_sum = 0

for game_number, results in games.items():
    impossible = [True for color in results.keys() if results[color] > cube_limit[color]]
    if not True in impossible:
        possible_games_sum += game_number
print(possible_games_sum) 
