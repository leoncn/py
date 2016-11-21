from random import choice

class RandomWalk():
	"""A class to generate random walks."""

	def __init__(self, num_points=5000):
		"""Init atttributes of a walk"""
		self.num_points = num_points
		self.x_values = [0]
		self.y_values = [0]

	def fill(self):
		while len(self.x_values) < self.num_points:
			x_step = self.next_step()
			y_step = self.next_step()

			if(x_step and y_step):
				self.x_values.append(self.x_values[-1] + x_step)
				self.y_values.append(self.y_values[-1] + y_step)

	def next_step(self):
		direction = choice([-1,1])
		distance = choice(range(5))
		return direction * distance


