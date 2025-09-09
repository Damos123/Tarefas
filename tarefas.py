("""Funções de tarefas básicas.

Esta versão implementa `maximo(a, b, c)` que retorna o maior entre três inteiros.

Exemplos:
>>> maximo(0, -1, 1)
1
>>> maximo(5, 5, 2)
5
""")

def maximo(a: int, b: int, c: int) -> int:
	"""Retorna o maior entre três inteiros.

	A implementação usa comparações simples (sem usar built-in `max`) para
	manter o exercício didático.
	"""
	maior = a
	if b > maior:
		maior = b
	if c > maior:
		maior = c
	return maior


if __name__ == '__main__':
	# Executa os doctests embutidos no módulo (saída detalhada)
	import doctest
	doctest.testmod(verbose=True)

