"""Self check"""

import random
import string


def generate_string(n=26):
	"""Choose random letters with space until given string"""
	character_pool = string.ascii_lowercase + ' '

	res = ''
	for i in range(n):
		res += character_pool[random.randrange(27)]

	return res


def score(goal, test_string):
	"""Percentage of matched characters"""
	num_same = 0

	for i, v in enumerate(goal):
		if goal[i] == test_string[i]:
			num_same += 1

	return num_same / len(goal)


def generate_char():
	"""Generate random letters"""
	character_pool = string.ascii_lowercase + ' '
	return character_pool[random.randrange(27)]


def replace_char(goal, test_string):
	"""Check"""
	for i, v in enumerate(goal):
		if goal[i] == test_string[i]:
			continue
		elif goal[i] != test_string[i] and i == 0:
			return generate_char() + test_string[i + 1:]
		else:
			return test_string[:i] + generate_char() + test_string[i + 1:]

	return test_string


def worker():
	"""Random guess"""
	# define work left
	incorrect_string_length = 28

	# string params
	goal_string = 'methinks it is like a weasel'
	new_string = generate_string(incorrect_string_length)

	# save score for plotting
	score_best = 0
	score_new = score(goal_string, new_string)

	retry = 0
	# main loop
	while str_score := score_new < 1:
		# return best score so far
		if score_new > score_best:
			print(score_new, new_string)
			score_best = score_new

		new_string = generate_string(28)
		score_new = score(goal_string, new_string)
		retry += 1

		# print best in 1 million
		if retry % 1000000 == 0:
			print(f'Best in {retry}: {score_best} - {new_string}')

	return new_string


def worker2():
	"""Hill climbing algorithm"""
	# define work left
	incorrect_string_length = 28

	# string params
	goal_string = 'methinks it is like a weasel'
	new_string = generate_string(incorrect_string_length)

	# save score for plotting
	score_best = 0
	score_new = score(goal_string, new_string)

	# main loop
	while score_new < 1:
		# return best score so far
		if score_new > score_best:
			print(score_new, new_string)
			score_best = score_new

		new_string = replace_char(goal_string, new_string)
		score_new = score(goal_string, new_string)

	return score_new, new_string


def main():
	# for i in range(32):
	# 	t = threading.Thread(target=worker)
	# 	t.start()

	print(worker2())


if __name__ == '__main__':
	main()
