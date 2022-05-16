"""Solve sudoku"""


class Sudoku:

	def __init__(self, grid):
		# check for correct input type
		if not isinstance(grid, list):
			raise RuntimeError('Require a list of lists')
		for line in grid:
			if not isinstance(line, list):
				raise RuntimeError('Require a list of lists')

		# check for correct input values
		self.grid = grid
		self.size = len(grid)
		if self.size % 3 != 0:
			raise RuntimeError('Number of row is not divisible by 3')
		for line in grid:
			if len(line) != self.size:
				raise RuntimeError('Number of columns and rows do not match')
			elif len(line) % 3 != 0:
				raise RuntimeError('Number of column is not divisible by 3')
			else:
				for item in line:
					if not (0 <= item <= 9):
						raise RuntimeError('Number not between 0 and 9')

	def __str__(self):
		grid_str = '=' * self.size * 2 + '\n'
		for row in self.grid:
			grid_str += ' '.join([str(item) for item in row]) + '\n'
		grid_str += '=' * self.size * 2 + '\n'
		return grid_str

	def __repr__(self):
		return f'Sudoku({self.grid})'

	def possible(self, row, col, num):
		# check num in row
		for x in range(self.size):
			if self.grid[row][x] == num:
				return False

		# check num in col
		for y in range(self.size):
			if self.grid[y][col] == num:
				return False

		# check num in the square
		x0 = (col // 3) * 3
		y0 = (row // 3) * 3
		for i in range(0, 3):
			for j in range(0, 3):
				if self.grid[y0 + i][x0 + j] == num:
					return False

		return True

	def solve(self):
		for y in range(self.size):
			for x in range(self.size):
				if self.grid[y][x] == 0:
					for n in range(1, self.size + 1):
						if self.possible(y, x, n):
							self.grid[y][x] = n
							self.solve()
							self.grid[y][x] = 0
					return
		return print(Sudoku(self.grid))


def main():
	grid = [
		[2, 5, 0, 0, 3, 0, 9, 0, 1],
		[0, 1, 0, 0, 0, 4, 0, 0, 0],
		[4, 0, 7, 0, 0, 0, 2, 0, 8],
		[0, 0, 5, 2, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 9, 8, 1, 0, 0],
		[0, 4, 0, 0, 0, 3, 0, 0, 0],
		[0, 0, 0, 3, 6, 0, 0, 7, 2],
		[0, 7, 0, 0, 0, 0, 0, 0, 3],
		[9, 0, 3, 0, 0, 0, 6, 0, 4]
	]

	sudoku = Sudoku(grid)
	print(sudoku.solve())
	print(sudoku)


if __name__ == '__main__':
	main()
