#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# File: p7.py
# Description: http://projecteuler.net/problem=7
#

from math import ceil, sqrt
import time

def is_square(N):
	return sqrt(N).is_integer()

def is_prime(number):

	a = ceil(sqrt(number))
	b2 = pow(a, 2) - number
	i=0
	while not is_square(b2):
		a += 1
		b2 = pow(a, 2) - number

	return (a - sqrt(b2) == 1 and a + sqrt(b2) == number)

start_time = time.time()
print "Começando a execução em: %s" % start_time
n = 3
primos = []
while True:
	if len(primos) == 10000:
		break
	if is_prime(n):
		print "t = %.2fs ----> Mais um primo encontrado: %d" % (time.time() - start_time, n) 
		primos.append(n)
	n += 2

print primos[-1]
print time.time() - start_time, "seconds"
