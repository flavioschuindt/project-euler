

palindros = set()
for i in range(100, 1000):
	for p in range(i, 1000):
		mult = i * p
		if int(str(mult)[::-1]) == mult:
			palindros.add(mult)

for palindro in sorted(palindros):
	maior = palindro

print maior