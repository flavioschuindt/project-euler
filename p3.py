#
# File: p3.py
# Description: http://projecteuler.net/problem=3
#
from math import ceil, sqrt, pow

# The solution below is impossible to calculate! You have to use Fermat factorization method!
'''number = 600851475143
i = 1

while True:
	if number % i == 0:
		print i
	print i
	i += 1
	if i == number + 1:
		break'''

# Using Fermat

def is_square(N):
	return sqrt(N).is_integer()

def decomposition(number):

	a = ceil(sqrt(number))
	b2 = pow(a, 2) - number
	i=0
	while not is_square(b2):
		#i = i +1
		#print i
		a += 1
		b2 = pow(a, 2) - number

	return [a - sqrt(b2), a + sqrt(b2)]

number = 600851475143
ret = decomposition(number)

print ret

ret_lower = ret[0]
ret_upper = ret[1]

while True:
	ret_lower_b = decomposition(ret_lower)[0]
	if decomposition(ret_lower)[0] == ret_lower:
		#fim

	
