

current_depth = 0
current_h_pos = 0
aim = 0

with open('day_02_puzzle_input.txt') as f:
    lines = f.readlines()
    for line in lines:
        # fowards
        if "fo" == line[0:2]:
            current_h_pos += int(line[8:])
            current_depth += (int(line[8:]) * aim)
        # down
        elif "do" == line[0:2]:
            aim += int(line[5:])

        elif "up" == line[0:2]:
            aim -= int(line[3:])

print(current_h_pos)
print(current_depth)
print(current_h_pos*current_depth)

