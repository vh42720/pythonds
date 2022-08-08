import random

from chapter_4.queue import Queue


class Printer:
	def __init__(self, ppm):
		self.pagerate = ppm
		self.currentTask = None
		self.timeRemaining = 0

	def tick(self):
		if self.currentTask is not None:
			self.timeRemaining -= 1
			if self.timeRemaining <= 0:
				self.currentTask = None

	def busy(self):
		if self.currentTask is not None:
			return True
		else:
			return False

	def startNext(self, newTask):
		self.currentTask = newTask
		self.timeRemaining = newTask.getPages() * 60 / self.pagerate


class Task:
	def __init__(self, time):
		self.timestamp = time
		self.pages = random.randrange(1, 21)

	def getStamp(self):
		return self.timestamp

	def getPages(self):
		return self.pages

	def waitTime(self, currentTime):
		return currentTime - self.timestamp


def printerSimulation(numSeconds, pagesPerMinute):
	"""Simulation of printer wait time"""

	labPrinter = Printer(pagesPerMinute)
	printQueue = Queue()
	waitingTimes = []

	for currentSecond in range(numSeconds):
		if newPrintTask():
			task = Task(currentSecond)
			printQueue.enqueue(task)

		if (not labPrinter.busy()) and (not printQueue.isEmpty()):
			nextTask = printQueue.dequeue()
			waitingTimes.append(nextTask.waitTime(currentSecond))
			labPrinter.startNext(nextTask)

		labPrinter.tick()

	averageWait = sum(waitingTimes) / len(waitingTimes)
	print(f'Average wait {averageWait:6.2f} sec {printQueue.size():3d} task remaining')


def newPrintTask():
	return random.randrange(1, 181) == 180


def main():
	for i in range(10):
		printerSimulation(3600, 10)


if __name__ == '__main__':
	main()
