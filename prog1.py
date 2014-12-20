"""
	Program 1: Using Python Lists
"""

import sys

nx = 20
nt = 50
dt = 0.01
c = 1
dx = 2.0 / (nx-1)

u = []

for i in range(0,nx):
	print >> sys.stdout, i

	x = 0 + i * dx
	print >> sys.stdout, x

	if x <= 1 and x >= 0.5:
		u.append(2)
	else:
		u.append(1)

print >> sys.stdout, u
