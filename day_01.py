direction_map = {
    # e.g. Facing North: if I turn Left I face West, if I turn Right I face East
    'N': {'L': 'W', 'R': 'E'},
    'E': {'L': 'N', 'R': 'S'},
    'S': {'L': 'E', 'R': 'W'},
    'W': {'L': 'S', 'R': 'N'},
}

# Starting condition
position_x, position_y = 0, 0
current_direction = 'N'

# Sample Input
input_text = 'R2, R2, R2'
for instruction in input_text.split(', '):
    left_right = instruction[0]     # 'L' or 'R'
    step_text = instruction[1:]     # '2'
    steps = int(step_text)

    # Execute the instruction
    new_direction = direction_map[current_direction][left_right]
    if new_direction == 'N':
        position_y = position_y + steps     # Go north
    elif new_direction == 'S':              
        position_y = position_y - steps     # Go south
    elif new_direction == 'E':
        position_x = position_x + steps     # Go east
    elif new_direction == 'W':
        position_x = position_x - steps     # Go west
    else:
        print(f'Wrong direction: {new_direction}')
    # Record the new direction
    current_direction = new_direction

# Print result
print(f'Ending position: ({position_x}, {position_y})')
print(f'Distance: {abs(position_x) + abs(position_y)}')