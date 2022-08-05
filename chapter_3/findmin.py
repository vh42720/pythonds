import time
from random import randrange


def findmin(nums):
	min = nums[0]
	for num in nums:
		if num < min:
			min = num

	return min


def findmin_compare(nums):
	min = nums[0]
	for i in nums:
		for j in nums:
			if j < i:
				min = j

	return min


def main():
	for list_size in range(1000, 10001, 1000):
		my_list = [randrange(1000000) for x in range(list_size)]

		# O(n2)
		start = time.time()
		print(findmin_compare(my_list))
		end = time.time()
		print(f'size: {list_size} time: {end - start}')

		# O(n)
		start = time.time()
		print(findmin(my_list))
		end = time.time()
		print(f'size: {list_size} time: {end - start}')


if __name__ == '__main__':
	main()
