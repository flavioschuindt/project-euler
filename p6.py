
soma_quadrado = 0
soma = 0
for n in range(1, 101):
	soma_quadrado += pow(n, 2)
	soma += n
	print soma_quadrado, soma

diff = pow(soma, 2) - soma_quadrado
print diff