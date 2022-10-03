class Deque:

	def __init__(self):
		self.items = []

	def addFront(self, item):
		self.items.append(item)

	def addRear(self, item):
		self.items.insert(0, item)

	def removeFront(self):
		return self.items.pop()

	def removeRear(self):
		return self.items.pop(0)

	def isEmpty(self):
		return self.items == []

	def size(self):
		return len(self.items)
