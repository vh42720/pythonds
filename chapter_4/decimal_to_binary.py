from chapter_4.stack import Stack


def toBinary(decNum, base):
	digits = '0123456789ABCDEF'
	remStack = Stack()

	while decNum > 0:
		rem = decNum % base
		remStack.push(rem)
		decNum //= base

	binString = ''
	while not remStack.isEmpty():
		binString += digits[remStack.pop()]

	return binString


def main():
	print(toBinary(25, 2))
	print(toBinary(25, 8))
	print(toBinary(256, 16))
	print(toBinary(26, 26))


if __name__ == '__main__':
	main()
