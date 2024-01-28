keypad = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
coordinate_map = {
    'U': (0, -1),
    'D': (0, 1),
    'L': (-1, 0),
    'R': (1, 0)
}

# Read input from file
with open('day_02.txt', 'r') as file_obj:
    input_text = file_obj.read()

position = (1, 1)
bathroom_code = ''
for instruction in input_text.splitlines():
    # e.g. instruction = 'ULL'
    for letter in instruction:
        # e.g. letter = 'U' then x_adjustment is 0, y_adjustment is -1
        x_adjustment, y_adjustment = coordinate_map[letter] 
        # position change from (1, 1) to (1, 0)
        position_x = (position[0] + x_adjustment)
        position_y = (position[1] + y_adjustment)
        # Boundary check (x and y coordinates can only be 0, 1 or 2)
        position_x = min(max(0, position_x), 2)
        position_y = min(max(0, position_y), 2)
        # Set the new position
        position = (position_x, position_y)
    # Finish processing 1 instruction
    bathroom_code = bathroom_code + str(keypad[position_y][position_x])
print(f'Bathroom code: {bathroom_code}')