"""Cards simulation"""


class Card:

	def __init__(self, suit, num):
		self.suit = suit
		self.num = num

	def __repr__(self):
		return f'Card(suit={self.suit}, num={self.num})'

	def __str__(self):
		return f'{self.num} of {self.suit}'


class
