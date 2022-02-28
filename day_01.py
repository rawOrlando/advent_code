
last_elev = None
current_window = list()
increased_elev_count = 0

# size does not seem to be a constrant here.
elevations = list()
with open('day_01_puzzle_input.txt') as f:
    lines = f.readlines()
    for line in lines:
    	elevations.append(int(line))

index = 3
while index < len(elevations):
	prev_sum = elevations[index - 3] + elevations[index - 2] + elevations[index - 1]
	next_sum = elevations[index] + elevations[index - 2] + elevations[index - 1]
	if prev_sum < next_sum:
		increased_elev_count = increased_elev_count + 1
	index = index + 1


print(increased_elev_count)



