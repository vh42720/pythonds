from chapter_4.deque import Deque


def pal_checker(string):
	char_deque = Deque()

	for char in string:
		char_deque.addFront(char)

	equal = True
	while char_deque.size() > 1 and equal:
		if char_deque.removeFront() != char_deque.removeRear():
			equal = False

	return equal


def main():
	print(pal_checker("lsdkjfskf"))
	print(pal_checker("radar"))


if __name__ == '__main__':
	main()
