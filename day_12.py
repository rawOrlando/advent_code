
class MyNode(object):

	def __init__(self, name):
		self.big = name.isupper()
		self.name = name
		self.connections = []

	def add_route(self, other_node):
		self.connections.append(other_node)

	def __str__(self):
		return self.name

	def __repr__(self):
		return self.__str__()

	def __eq__(self, obj):
		return isinstance(obj, MyNode) and obj.name == self.name

class Path():
	def __init__(self, _list):
		self.nodes = _list
		self.double_small_stop = False

	def can_add_node(self, node):

		if node.big:
			return True
		if not self.double_small_stop and not node.name == "start":
			return True
		if node not in self.nodes:
			return True
		return False

	def copy(self):
		cls = self.__class__
		result = cls.__new__(cls)
		result.nodes = self.nodes.copy()
		result.double_small_stop = self.double_small_stop
		return result

	def append(self, x):
		if not x.big and x in self.nodes:
			self.double_small_stop = True
		return self.nodes.append(x)

	def last_node(self):
		return self.nodes[-1]

	def __str__(self):
		return self.nodes.__str__()

class MyMap(object):
	"""
	Should have a list or Dict of Nodes
	"""

	def __init__(self):
		self.all_nodes = {}
		self.start = None
		self.end = None

	def add_route(self, str_node_1, str_node_2):
		if str_node_1 in self.all_nodes.keys():
			node_1 = self.all_nodes[str_node_1]
		else:
			node_1 = self._add_new_node(str_node_1)
		if str_node_2 in self.all_nodes.keys():
			node_2 = self.all_nodes[str_node_2]
		else:
			node_2 = self._add_new_node(str_node_2)

		node_1.add_route(node_2)
		node_2.add_route(node_1)

	def _add_new_node(self, str_node):
		node = MyNode(str_node)
		self.all_nodes[str_node] = node

		if str_node == "start":
			self.start = node

		if str_node == "end":
			self.end = node

		return node

	def find_all_paths(self):
		return self._find_all_paths(Path([self.start]))

	def _find_all_paths(self, current_path):
		paths = []
		for connection in current_path.last_node().connections:
			new_path = current_path.copy()
			# No repeat small tunnels
			if new_path.can_add_node(connection):
				print(connection)
				print(new_path)
				new_path.append(connection)
				if connection == self.end:
					print("End of the path")
					paths.append(new_path)
				else:
					for path in self._find_all_paths(new_path):
						paths.append(path)

		return paths

node_map = MyMap()

# Read numbers
with open('day_12_puzzle_input.txt') as f:

    lines = f.readlines()
    for line in lines:
    	line_split = line.strip().split("-")
    	node_map.add_route(line_split[0], line_split[1])


    print("Answer")
    paths = node_map.find_all_paths()
    for path in paths:
    	print(path)
    print(len(paths))
