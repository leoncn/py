import matplotlib.pyplot as plt
max = 11
values = list(range(max))
squares = [ i**2 for i in values ]
plt.plot(values, squares, linewidth=3)
plt.title('first n squares') , plt.xlabel('value'), plt.ylabel('square')
#plt.show()

if( 0 and 1):
	print 'closed'