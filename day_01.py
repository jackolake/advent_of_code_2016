direction_map = {
    # e.g. Facing North: if I turn Left I face West, if I turn Right I face East
    'N': {'L': 'W', 'R': 'E'},
    'E': {'L': 'N', 'R': 'S'},
    'S': {'L': 'E', 'R': 'W'},
    'W': {'L': 'S', 'R': 'N'},
}
coordinate_map = {
    'N': (0, 1),
    'S': (0, -1),
    'E': (1, 0),
    'W': (-1, 0)
}

# Starting condition
position_x, position_y = 0, 0
current_direction = 'N'
visited_positions = []  # List of positions (x, y)

# Read input from file
with open('day_01.txt', 'r') as file_obj:
    input_text = file_obj.read()

for instruction in input_text.split(', '):
    left_right = instruction[0]     # 'L' or 'R'
    step_text = instruction[1:]     # '2'
    steps = int(step_text)

    # Execute the instruction
    new_direction = direction_map[current_direction][left_right]
    coordinate_adjustment = coordinate_map[new_direction]
    for step in range(steps):
        x_adjustment, y_adjustment = coordinate_adjustment
        position_x = position_x + x_adjustment
        position_y = position_y + y_adjustment
        visited_positions.append((position_x, position_y))
    # Record the new direction
    current_direction = new_direction
# Print result
print(f'Ending position: ({position_x}, {position_y})')
print(f'Distance: {abs(position_x) + abs(position_y)}')