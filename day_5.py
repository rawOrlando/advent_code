
from collections import defaultdict


def add_steam_for_line(dict_steam, x1, y1, x2, y2):

	if x1 == x2:
		index = 0
		y_max = max(y1, y2)
		y_min = min(y1, y2)
		while index + y_min <= y_max:
			dict_steam[(x1,index + y_min)] += 1
			index += 1

	elif y1 == y2:
		index = 0
		x_max = max(x1, x2)
		x_min = min(x1, x2)
		while index + x_min <= x_max:
			dict_steam[(index + x_min, y1)] += 1
			index += 1

	else:
		index = 0
		x_direction = abs(x2-x1)/(x2-x1)
		y_direction = abs(y2-y1)/(y2-y1)
		while (x2-x1)*x_direction >= index:
			dict_steam[(index * x_direction + x1, index * y_direction + y1)] += 1
			index += 1

	return dict_steam


dict_steam = defaultdict(int)

with open('day_5_puzzle_input.txt') as f:
    lines = f.readlines()

    for line in lines:
    	# add vent data
    	comp = line.split()
    	cordiate_1 = comp[0].split(",")
    	cordiate_2 = comp[2].split(",")
    	x1 = int(cordiate_1[0])
    	y1 = int(cordiate_1[1])
    	x2 = int(cordiate_2[0])
    	y2 = int(cordiate_2[1])
    	dict_steam = add_steam_for_line(dict_steam, x1, y1, x2, y2 )

count = 0
for item in dict_steam.values():
	if item > 1:
		count = count + 1

print (count)


