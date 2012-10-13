#
# File: 1.py
# Description: http://projecteuler.net/problem=2
#

ok = True
anteriores = [1, 2]
soma = 2

while ok:
	novo = sum(anteriores)
	if novo <= 4000000:
		anteriores[0] = anteriores[1]
		anteriores[1] = novo
		if novo % 2 == 0:
			soma += novo
	else:
		ok = False
print soma