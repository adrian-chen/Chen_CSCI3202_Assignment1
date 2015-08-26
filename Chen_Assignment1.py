import collections

class Queue(object):
	def __init__(self):
		self.myqueue = []
	def push(self, argument):
		if isinstance(argument, (int, long)):
			return self.myqueue.append(argument)
		else:
			print "Queue doesn't accept non-integers."
	def deque(self):
		return self.myqueue.pop(0)

def test_Queue():
	print "===== QUEUE TEST ====="
	this_queue = Queue()
	for i in range(10):
		this_queue.push(i)	# Add 10 integers
	for i in range(10):
		print this_queue.deque()		# Deque the integers

class Stack(object):
	def __init__(self):
		self.my_stack = collections.deque()
	def push(self, argument):
		if isinstance(argument, (int, long)):
			return self.my_stack.append(argument)
		else:
			print "Stack doesn't accept non-integers."
	def pop(self):
		return self.my_stack.pop()
	def checkSize(self):
		return len(self.my_stack)

def test_Stack():
	print "===== STACK TEST ====="
	this_stack = Stack()
	for i in range(10):
		this_stack.push(i)	# Add 10 integers
	for i in range(10):
		print this_stack.pop()		# Deque the integers

class BinaryNode(object):
	def __init__(self, value, parent_value):
		self.key = value
		self.left = None
		self.right = None
		self.parent = parent_value

class BinaryTree(object):
	def __init__(self):
		self.root = None

	def add(self, value, parent_value):
		if self.root == None:
			self.root = BinaryNode(value, None)
		else:
			found_node = self.search(self.root, parent_value)
			if found_node == None:
				print "Parent not found"
			elif found_node.left == None:
				found_node.left = BinaryNode(value, found_node)
			elif found_node.right == None:
				found_node.right = BinaryNode(value, found_node)
			else:
				print "Parent has two children, node not added"

	def delete(self, value):
		del_node = self.search(self.root, value)
		if (del_node.left is None) and (del_node.right is None):
			if del_node is del_node.parent.left:
				del_node.parent.left = None
			else:
				del_node.parent.right = None

	def search(self, node, keyValue):
		if node is not None:
			if node.key == keyValue:
				return node
			else:
				left_search = self.search(node.left, keyValue)
				right_search = self.search(node.right, keyValue)
				if left_search is not None:
					return left_search
				elif right_search is not None:
					return right_search

	def printy(self):
		print("Printing Tree")
		if self.root != None:
			print self.root.key
			self.recursive_print(self.root.left)
			self.recursive_print(self.root.right)

	def recursive_print(self, node):
		if node is not None:
			print node.key
			self.recursive_print(node.left)
			self.recursive_print(node.right)

def test_Binary_Tree():
	print "===== BINARY TREE TEST ====="
	this_tree = BinaryTree()
	this_tree.add(1, 8)
	this_tree.add(2, 1)
	this_tree.add(3, 1)
	this_tree.add(4, 2)
	this_tree.add(5, 2)
	this_tree.add(6, 3)
	this_tree.add(7, 3)
	this_tree.add(8, 4)
	this_tree.add(9, 4)
	this_tree.add(10, 5)
	this_tree.printy()
	this_tree.delete(10)
	this_tree.delete(6)
	this_tree.printy()

class Vertex(object):
	def __init__(self, keyValue):
		self.key = keyValue
		self.adjacent_dict = {}

class Graph(object):
	def __init__(self):
		self.dictionary = {}

	def add(self, value):
		if self.dictionary.has_key(value):
			print "Vertex already exists"
		else:
			self.dictionary[value] = Vertex(value)

	def findVertex(self, value):
		print self.dictionary[value].adjacent_dict.keys()

	def add_edge(self, value1, value2):
		if self.dictionary.has_key(value1) and self.dictionary.has_key(value2):
			self.dictionary[value1].adjacent_dict[value2] = "Linked"

def test_Graph():
	print "===== GRAPH TEST ====="
	this_graph = Graph()
	for i in range(10):
		this_graph.add(i)
	for i in range(9):
		this_graph.add_edge(i, i+1)
	for i in range(8):
		this_graph.add_edge(i, i+2)
	for i in range(7):
		this_graph.add_edge(i, i+3)
	for i in range(5):
		this_graph.findVertex(i)


if __name__ == "__main__":
	test_Queue()
	test_Stack()
	test_Binary_Tree()
	test_Graph()