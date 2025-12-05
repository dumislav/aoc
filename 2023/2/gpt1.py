# Define the maximum number of each colored cube
max_cubes = {'red': 12, 'green': 13, 'blue': 14}

# Parse each game line and extract the cube details
def parse_game_line(game_line):
    game_id, raw_draws = game_line.split(':', 1)
    draws = raw_draws.strip().split(';')
    
    game_info = {'id': int(game_id.replace('Game', '').strip()), 'draws': []}
    
    for draw in draws:
        draw_info = {}
        for cube_info in draw.split(','):
            number, color = cube_info.strip().split()
            draw_info[color] = int(number)
        game_info['draws'].append(draw_info)
    return game_info

# Check if a game is possible with given max_cubes
def is_game_possible(game, max_cubes):
    for draw in game['draws']:
        for color, number in draw.items():
            if number > max_cubes[color]:
                return False
    return True

# Read the input file and process each game
with open('input.txt', 'r') as file:
    possible_game_ids = []
    for line in file:
        game = parse_game_line(line.strip())
        if is_game_possible(game, max_cubes):
            possible_game_ids.append(game['id'])

# Sum up the IDs of the possible games and print the result
print("Sum of possible game IDs:", sum(possible_game_ids))