from operator import attrgetter

def is_wall(numbers_grid, x, y):
    max_x_point = len(numbers_grid)
    max_y_point = len(numbers_grid[0])

    if x < 0 or y < 0:
        return True

    max_x_point = len(numbers_grid)
    max_y_point = len(numbers_grid[0])
    if x >= max_x_point or y >= max_y_point:
        return True

    if numbers_grid[x][y] == 9:
        return True

    else:
        return False

class Basin(object):

    """docstring for Basin"""
    def __init__(self, number_grid, low_point_x, low_point_y):
        super(Basin, self).__init__()

        # set of points that have had there sides checked
        # and points that have not seen what was on there sides
        self.points = set()
        self.unchecked_points = []
        self.numbers_grid = numbers_grid
        self.unchecked_points.append((low_point_x, low_point_y))
        self.lowest_point = (low_point_x, low_point_y)

        while self.unchecked_points:
            self._explore_()

    def valid_basin(self):
        print("valid_basin")
        print(self.lowest_point[0])
        print(self.lowest_point[1])
        supposed_lowest = self.numbers_grid[self.lowest_point[0]][self.lowest_point[1]]
        for point in self.points:
            if supposed_lowest > self.numbers_grid[point[0]][point[1]]:
                return False

        # todo what about basins with equal low points.
        return True


    def _explore_(self):
        point = self.unchecked_points.pop()

        neighbors = self._get_non_wall_neighbors_(point[0], point[1])

        for neighbor in neighbors:
            if (neighbor not in self.points and
               neighbor not in self.unchecked_points):
               self.unchecked_points.append(neighbor)

        self.points.add(point)


    def _get_non_wall_neighbors_(self, x, y):
        neighbors = []
        new_x = x + 1
        new_y = y
        if not is_wall(self.numbers_grid, new_x, new_y):
            neighbors.append((new_x, new_y))
        new_x = x - 1
        new_y = y
        if not is_wall(self.numbers_grid, new_x, new_y):
            neighbors.append((new_x, new_y))
        new_x = x
        new_y = y + 1
        if not is_wall(self.numbers_grid, new_x, new_y):
            neighbors.append((new_x, new_y))
        new_x = x
        new_y = y - 1
        if not is_wall(self.numbers_grid, new_x, new_y):
            neighbors.append((new_x, new_y))

        return neighbors

    def size(self):
        return len(self.points)



def is_lowest_neighbors(numbers_grid, x, y):
    max_x_point = len(numbers_grid)
    max_y_point = len(numbers_grid[0])

    if x+1 < max_x_point and numbers_grid[x][y] >= numbers_grid[x+1][y]:
        return False

    if y+1 < max_y_point and numbers_grid[x][y] >= numbers_grid[x][y+1]:
        return False

    if y-1 > -1 and numbers_grid[x][y] >= numbers_grid[x][y-1]:
        print(numbers_grid[x][y])
        print(numbers_grid[x][y-1])
        return False

    if x-1 > -1 and numbers_grid[x][y] >= numbers_grid[x-1][y]:
        return False

    return True



numbers_grid = list()

# Read numbers
with open('day_9_puzzle_input.txt') as f:

    lines = f.readlines()
    for line in lines:
        row = list()
        for number in line:
            if number != '\n':
                row.append(int(number))
        numbers_grid.append(row)

x_index = 0
total = 0
basins = []
while x_index < len(numbers_grid):
    y_index = 0
    while y_index < len(numbers_grid[x_index]):
        if is_lowest_neighbors(numbers_grid, x_index, y_index):
            basin = Basin(numbers_grid, x_index, y_index)
            if basin.valid_basin():
                basins.append(basin)
            total = total + numbers_grid[x_index][y_index] + 1

        y_index += 1
    x_index += 1

print(total)
print(len(basins))

basins.sort(key=lambda x: x.size(), reverse=True)

print(basins[0].size())
print(basins[1].size())
print(basins[2].size())
print(basins[0].size() * basins[1].size() * basins[2].size())




