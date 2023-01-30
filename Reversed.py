# Reversed
'''OBS: Não confunda com a função reverse() que estudamos nas lista e está só funciona em listas.
Já a função reversed() funciona com qualquer iterável.
Sua função é inverter o iterável.
A função reversed() retorna um iterável chamado List Reverse Iterator
   # exemplo
lista = [1, 2, 3, 4, 5, 6]
res = reversed(lista)
print(res)
print(type(res))
# Podemos converter o elemento retornado para uma lista, Tupla ou conjunto

# Lista
print(list(reversed(lista)))

# Tuple
print(tuple(reversed(lista)))

# Conjunto (set) Obs: em conjuntos não definimos a ordem dos elementos
print(set(reversed(lista)))

# Podemos iterar sobre o reversed()
for letra in reversed('Geek University'):
    print(letra, end='')

# podemos fazer o mesmo sem o uso do for
print(''.join(list(reversed('Geek University'))))

# já vimos como fazer isso mais fácil com o slice de strings
print('Geek university'[::-1])

# Podemos também utilizar o reversed() para fazer um loop for reverso
for n in reversed(range(0, 10)):
    print(n)

# Apesar que também já vimos como fazer isso utilizando o próprio range()
for n in range(9, -1, -1):
    print(n)  '''
