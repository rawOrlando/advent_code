from collections import defaultdict
from operator import attrgetter

class MyNode(object):

    def __init__(self, x, y, risk_value):
        self.x = x
        self.y = y
        self.risk_value = risk_value
        self.connections = []

    def add_route(self, other_node):
        self.connections.append(other_node)

    def get_coordinate(self):
        return (self.x, self.y)

    def __str__(self):
        return str((self.x, self.y))

    def __repr__(self):
        return self.__str__()

    def __eq__(self, obj):
        return isinstance(obj, MyNode) and obj.x == self.x and obj.y == self.y

def connect_node(x, y, risk_map):
    if (x, y) not in risk_map.keys():
        return

    if (x, y-1) in risk_map.keys():
        risk_map[(x, y-1)].add_route(risk_map[(x, y)])
        risk_map[(x, y)].add_route(risk_map[(x, y-1)])

    if (x-1, y) in risk_map.keys():
        risk_map[(x-1, y)].add_route(risk_map[(x, y)])
        risk_map[(x, y)].add_route(risk_map[(x-1, y)])


def BFS(start_point, ending_node, risk_map):

    vistited = defaultdict(lambda:False)

    # queue !?!
    queue = []

    vistited[start_point.get_coordinate()] = True
    queue.append(start_point)
    distance = 0

    while queue:
        moving_to = []
        index = 0
        distance += 1
        while index < len(queue):
            node = queue[index]
            node.risk_value -= 1
            if node.risk_value == 0:
                # todo do I need this
                #queue[index] = node
                moving_to.append(queue.pop(index))
                index -= 1
            index += 1

        for node in moving_to:
            for new_node in node.connections:
                if not vistited[new_node.get_coordinate()]:
                    queue.append(new_node)
                    vistited[new_node.get_coordinate()] = True

                if new_node is ending_node:
                    distance += new_node.risk_value - 1
                    return distance


def expand_map(original_risk_map, width, height):
    new_risk_map = original_risk_map.copy()

    x = 0
    while x < 5:
        y = 0
        while y < 5:
            if x == 0 and y == 0:
                y += 1
                continue
            for node in list(original_risk_map.values()):
                coordinate = node.get_coordinate()
                new_x = (x * width) + coordinate[0]
                new_y = (y * height) + coordinate[1]
                increased_risk = x + y
                new_risk = original_risk_map[coordinate].risk_value + increased_risk
                while new_risk > 9:
                    new_risk -= 9
                new_risk_map[(new_x, new_y)] = MyNode(new_x, new_y, new_risk)
                connect_node(new_x, new_y, new_risk_map)
            y += 1
        x += 1

    return new_risk_map


risk_map = {} #Map for (x, y) tuple to node
ending_node = None
# Read numbers
with open('day_15_puzzle_input.txt') as f:

    lines = f.readlines()
    index_x = 0
    for line in lines:
        index_y = 0
        line = line.strip()
        for character in line:
            risk_map[(index_x, index_y)] = MyNode(index_x, index_y, int(character))
            connect_node(index_x, index_y, risk_map)
            ending_node = risk_map[(index_x, index_y)]
            index_y += 1
        index_x += 1


risk_map = expand_map(risk_map, index_x, index_y)
ending_node = risk_map[(index_x*5-1, index_y*5-1)]


risk_level = 0
starting_node = risk_map[(0, 0)]

x = 0


print(BFS(start_point=starting_node,ending_node=ending_node, risk_map=risk_map))

