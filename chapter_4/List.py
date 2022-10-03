class Node:
	def __init__(self, initdata):
		self.data = initdata
		self.next = None

	def getData(self):
		return self.data

	def getNext(self):
		return self.next

	def setData(self, newdata):
		self.data = newdata

	def setNext(self, newnext):
		self.next = newnext


class UnorderedList:
	def __init__(self):
		self.head = None
		self.tail = None

	def isEmpty(self):
		return self.head is None

	def add(self, item):
		temp = Node(item)
		temp.setNext(self.head)
		if self.tail is None:
			self.tail = temp

		self.head = temp

	def size(self):
		current = self.head
		count = 0
		while current:
			count += 1
			current = current.getNext()

		return count

	def search(self, item):
		current = self.head
		found = False
		while current and not found:
			if current.getData() == item:
				found = True
			else:
				current = current.getNext()

		return found

	def remove(self, item):
		current = self.head
		previous = None
		found = False
		while not found:
			if current.getData() == item:
				found = True
			else:
				previous = current
				current = current.getNext()

		if current.getNext() is None:
			self.tail = previous

		if previous is None:
			self.head = current.getNext()
		else:
			previous.setNext(current.getNext())

	def append(self, item):
		# current = self.head
		# if current:
		# 	while current.getNext():
		# 		current = current.getNext()
		# 	current.setNext(Node(item))
		# else:
		# 	self.head = Node(item)
		#
		# current = self.head

		current = self.tail
		current.setNext(Node(item))


my_list = UnorderedList()
my_list.add(3)
my_list.add(2)
my_list.add(1)
my_list.remove(3)

print(my_list.size())
print(my_list.tail.getData())
print(my_list.head.getData())
