#!/usr/bin/env python
def prtnumtype(num):
	print num, 'is',
	if isinstance(num, (int, long, float, complex)):
		print type(num).__name__
	else:
		print 'not a number '


prtnumtype(1), prtnumtype('1x')