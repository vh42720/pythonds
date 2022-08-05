class Stack:
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def peek(self):
		return self.items[len(self.items) - 1]

	def size(self):
		return len(self.items)


def revstring(mystr):
	"""Reverse string using Stack"""
	str_stack = Stack()
	str_res = ''

	for i in mystr:
		str_stack.push(i)
	while not str_stack.isEmpty():
		str_res += str_stack.pop()

	return str_res


def stack_test():
	s = Stack()
	print(s.isEmpty())
	s.push(4)
	s.push('dog')
	print(s.peek())
	s.push(True)
	print(s.size())
	print(s.isEmpty())
	s.push(8.4)
	print(s.pop())
	print(s.pop())
	print(s.size())


def revstring_test():
	print(revstring('abcde'))
	print(revstring('apple'))
	print(revstring('x'))
	print(revstring('123456789'))


if __name__ == '__main__':
	revstring_test()
