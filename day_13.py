
paper = set()

read_switch = False
folds = []
# Read numbers
with open('day_13_puzzle_input.txt') as f:

    lines = f.readlines()
    for line in lines:
        line = line.strip()
        if not line:
            read_switch = True
        elif not read_switch:
            # mark point
            # todo rethink data structure
            paper.add(tuple(map(int, line.split(','))))
        elif read_switch:
            if "y=" in line:
                folds.append(("y", int(line.split("=")[-1])))
            elif "x=" in line:
                folds.append(("x", int(line.split("=")[-1])))

            # mark fold

print(paper)

print(len(paper))

# fold on y
# for point in paper.copy():
#     if point[1] > y_fold:
#         paper.remove(point)
#         difference = point[1] - y_fold
#         new_y = y_fold - difference
#         paper.add((point[0], new_y))


for fold in folds:
    for point in paper.copy():
        if fold[0] == "x":
            if point[0] > fold[1]:
                paper.remove(point)
                difference = point[0] - fold[1]
                new_x = fold[1] - difference
                paper.add((new_x, point[1]))
        if fold[0] == "y":
            if point[1] > fold[1]:
                paper.remove(point)
                difference = point[1] - fold[1]
                new_y = fold[1] - difference
                paper.add((point[0], new_y))

point_list = list(paper)
point_list.sort(key=lambda y: y[0])
point_list.sort(key=lambda y: y[1])
max_x = 0
max_y = 0
for point in point_list:
    if max_y < point[1] + 1:
        max_y = point[1] + 1
    if max_x < point[0] + 1:
        max_x = point[0] + 1
print(len(paper))
print(point_list)

y_index = -1
while y_index <= max_y:
    x_index = -1
    line = ""
    while x_index <= max_x:
        if (x_index, y_index) in paper:
            line += '#'
        else:
            line += '.'
        x_index += 1
    print(line)
    y_index += 1


