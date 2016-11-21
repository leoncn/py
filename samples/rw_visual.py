import matplotlib.pyplot as plt
from r_walk import RandomWalk

rw = RandomWalk()

rw.fill()
plt.scatter(rw.x_values, rw.y_values, edgecolor='none', \
 						c=list(range(rw.num_points)), cmap=plt.cm.Blues, s=15)
plt.show()


