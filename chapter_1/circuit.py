"""Circuit with Inheritance"""


class LogicGate:

	def __init__(self, n):
		self.label = n
		self.output = None

	def getLabel(self):
		return self.label

	def getOutput(self):
		self.output = self.performGateLogic()
		return self.output


class BinaryGate(LogicGate):

	def __init__(self, n):
		super(BinaryGate, self).__init__(n)

		self.pinA = None
		self.pinB = None

	def getPinA(self):
		if self.pinA is None:
			return int(input(f'Enter Pin A input for gate {self.getLabel()} ==>'))
		else:
			return self.pinA.getFrom().getOutput()

	def getPinB(self):
		if self.pinB is None:
			return int(input(f'Enter Pin B input for gate {self.getLabel()} ==>'))
		else:
			return self.pinB.getFrom().getOutput()

	def setNextPin(self, source):
		if self.pinA is None:
			self.pinA = source
		elif self.pinB is None:
			self.pinB = source
		else:
			print('Cannot Connect: NO EMPTY PINS on this gate')


class UnaryGate(LogicGate):

	def __init__(self, n):
		super(UnaryGate, self).__init__(n)
		self.pin = None

	def getPin(self):
		if self.pin is None:
			return int(input(f'Enter Pin input for gate {self.getLabel()} ==>'))
		else:
			return self.pin.getFrom().getOutput()

	def setNextPin(self, source):
		if self.pin is None:
			self.pin = source
		else:
			print('Cannot Connect: NO EMPTY PINS on this gate')


class AndGate(BinaryGate):

	def __init__(self, n):
		super(AndGate, self).__init__(n)

	def performGateLogic(self):

		a = self.getPinA()
		b = self.getPinB()
		if a == 1 and b == 1:
			return 1
		else:
			return 0


class OrGate(BinaryGate):

	def __init__(self, n):
		super(OrGate, self).__init__(n)

	def performGateLogic(self):
		a = self.getPinA()
		b = self.getPinB()
		if a == 0 and b == 0:
			return 0
		else:
			return 1


class XorGate(BinaryGate):

	def __init__(self, n):
		super(XorGate, self).__init__(n)

	def performGateLogic(self):
		a = self.getPinA()
		b = self.getPinB()
		if a == b:
			return 0
		else:
			return 1


class NotGate(UnaryGate):

	def __init__(self, n):
		super(NotGate, self).__init__(n)

	def performGateLogic(self):
		if self.getPin():
			return 0
		else:
			return 1


class Gate(UnaryGate):

	def __init__(self, n):
		super(Gate, self).__init__(n)

	def performGateLogic(self):
		return self.getPin()


class NorGate(OrGate):

	def performGateLogic(self):
		if super().performGateLogic() == 1:
			return 0
		else:
			return 1


class NandGate(AndGate):

	def performGateLogic(self):
		if super().performGateLogic() == 1:
			return 0
		else:
			return 1


class Connector:

	def __init__(self, fgate, tgate):
		self.fromgate = fgate
		self.togate = tgate

		tgate.setNextPin(self)

	def getFrom(self):
		return self.fromgate

	def getTo(self):
		return self.togate


def main():

	# NOT (( A and B) or (C and D))
	g1 = AndGate('G1')
	g2 = AndGate('G2')
	g3 = OrGate('G3')
	g4 = NotGate('G4')
	c1 = Connector(g1, g3)
	c2 = Connector(g2, g3)
	c3 = Connector(g3, g4)
	print(g4.getOutput())

	# NOT(A and B) and NOT(C and D)
	f1 = NandGate('F1')
	f2 = NandGate('F2')
	f3 = AndGate('F3')
	d1 = Connector(f1, f3)
	d2 = Connector(f2, f3)
	print(f3.getOutput())


def half_adder():

	g1 = AndGate('G1')
	g2 = XorGate('G2')
	print(_sum := g1.getOutput())
	print(carry := g2.getOutput())


def full_adder():
	g1 = XorGate('G1')
	g2 = AndGate('G2')
	g3 = XorGate('G3')
	g4 = Gate('G4')
	c1 = Connector(g1, g4)


if __name__ == '__main__':
	half_adder()
