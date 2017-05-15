""" Simple priority queue for lazy boys """

class PQueue:
	def __init__(self):
		self.contents = []

	def __repr__(self):
		return(str(self.contents))

	def add(self, item):
		if len(self.contents) == 0:
			self.contents.append(item)
			return

		
		try:
			for i in range(len(self.contents)):
				if item < self.contents[i]:
					self.contents.insert(i, item)
					break
				elif i == len(self.contents) - 1:
					self.contents.append(item)
					break
		except TypeError:
			print("Queue only accepts classes of consistent type")


	def pop(self):
		retval = self.contents[0]
		self.contents = self.contents[1:]
		return retval

	def peek(self):
		return self.contents[0]

