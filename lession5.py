class Node(object):
	def __init__(self,value):
		self._children = []
		self._value = value
	def __iter__(self):
		return iter(self._children)
	def add_children(self,child):
		self._children.append(child)
	def __repr__(self):
		return "Node({!r})".format(self._value)
def code4_3_2():
	root = Node('root')
	child1 = Node('child1')
	child2 = Node('child2')
	root.add_children(child1)
	root.add_children(child2)
	for child in root:
		print(child)
def code4_3_2():
	num = 0
	for i in range(1,5):
		num+= 1
		yield num
		#print(">")
def dfs(root):
	yield root._value
	for child in root:
		yield from dfs(child)
	
def test():
	mylist = range(3)
	for i in mylist:
		yield i*i

class test(object):
	def __len__(self):
		return 3
if __name__ == '__main__':
	"""root = Node('root')
	child1 = Node('child1')
	child2 = Node('child2')
	root.add_children(child1)
	root.add_children(child2)
	subchild1 = Node('subchild1')
	subchild2 = Node('subchild2')
	child1.add_children(subchild1)
	child1.add_children(subchild2)
	for child in dfs(root):
		print(child)
	"""

	test1 = test()
	print(len(test1))