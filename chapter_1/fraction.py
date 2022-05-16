"""Fraction Class"""


class Fraction:
	"""Fraction class"""

	@staticmethod
	def gcd(m, n):
		while m % n != 0:
			old_m = m
			old_n = n

			m = old_n
			n = old_m % old_n
		return n

	def __init__(self, top, bottom):
		if isinstance(top, int) and isinstance(bottom, int):
			common = self.gcd(top, bottom)
			self.num = top // common
			self.den = bottom // common
		else:
			raise RuntimeError('`top` or `bottom` are not integer')

	def __str__(self):
		return str(self.num) + '/' + str(self.den)

	def __repr__(self):
		return f'Fraction({self.num}, {self.den})'

	def __add__(self, other):
		new_num = self.num * other.den + self.den * other.num
		new_den = self.den * other.den

		return Fraction(new_num, new_den)

	def __radd__(self, other):
		new_num = self.num * other.den + self.den * other.num
		new_den = self.den * other.den

		return Fraction(new_num, new_den)

	def __iadd__(self, other):
		new_num = self.num * other.den + self.den * other.num
		new_den = self.den * other.den
		common = self.gcd(new_num, new_den)

		self.num = new_num // common
		self.den = new_den // common

		return self

	def __sub__(self, other):
		new_num = self.num * other.den - self.den * other.num
		new_den = self.den * other.den

		return Fraction(new_num, new_den)

	def __mul__(self, other):
		new_num = self.num * other.num
		new_den = self.den * other.den

		return Fraction(new_num, new_den)

	def __truediv__(self, other):
		new_num = self.num * other.den
		new_den = self.den * other.num

		return Fraction(new_num, new_den)

	def __lt__(self, other):
		first_num = self.num * other.den
		second_num = other.num * self.den

		return first_num < second_num

	def __le__(self, other):
		first_num = self.num * other.den
		second_num = other.num * self.den

		return first_num <= second_num

	def __gt__(self, other):
		first_num = self.num * other.den
		second_num = other.num * self.den

		return first_num > second_num

	def __ge__(self, other):
		first_num = self.num * other.den
		second_num = other.num * self.den

		return first_num >= second_num

	def __eq__(self, other):
		first_num = self.num * other.den
		second_num = other.num * self.den

		return first_num == second_num

	def __ne__(self, other):
		first_num = self.num * other.den
		second_num = other.num * self.den

		return first_num != second_num

	def getNum(self):
		return self.num

	def getDen(self):
		return self.den


f1 = Fraction(1, -4)
f2 = Fraction(1, 2)
f3 = 3

print(f1 + f2)
f1 += f2
print(f1.__repr__())
# print(f1 == f2)
# print(f1 - f2)
# print(f1 * f2)
# print(f1 / f2)
# print(f1 < f2)
# print(f1 > f2)
# print(f1.getNum())
# print(f1.getDen())
