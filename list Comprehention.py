# list Comprehention
'''- Utilizando lis Comprehention nós podemos gerar novas listas com dados processados a partir de outro
interável.
 # Sintaxe de List Comprehension
[dado for dado in iterável]

numeros = [1, 2, 3, 4, 5]
res = [numero * 10 for numero in numeros]
print(res)
Para entender melhor o que está acontecendo devemos dividir a expressão em duas partes:
    - A primeiro parte: for numero in numeros
    - A segunda parte: numero * 10


res = [numero / 2 for numero in numeros]
print(res)

def funcao(valor):
    return valor * valor

res = [funcao(numero) for numero in numeros]
print(res)


# List Comprehention versus Loop

# loop
numeros = [1, 2, 3, 4, 5]
numeros_dobrados = []
for numero in numeros:
    numeros_dobrados.append(numero * 2)

print(numeros_dobrados)

# List Comprehension
print([numero * 2 for numero in numeros])

# Outros exemplos
nome = 'Geek University'
print([letra.upper() for letra in nome])

# 2

def caixa_alta(nome):
    nome = nome.replace(nome[0], nome[0].upper())
    return nome


amigos = ['maria', 'julia', 'pedro', 'guilherme', 'vanessa']
print([caixa_alta(amigo) for amigo in amigos])

# 3
print([numero * 3 for numero in range(1, 10)])

# 4
print([bool(valor) for valor in [0, [], True, 1, 3.14]])

# 5
print([str(numero)for numero in {1, 2, 3, 4, 5}])

Nós podemos adicionar estruturas condicionais lógicas às nossa List Comprehention

# Exemplos
# 1
numeros = [1, 2, 3, 4, 5, 6]
pares = [numero for numero in numeros if numero %2 ==0]
impares = [numero for numero in numeros if numero %2 != 0]

print(pares)
print(impares)

# Refatorando

# Qualquer número par em módulo de 2 é 0 e 0 em Python é False. not False = True
pares = [numero for numero in numeros if not numero % 2]
# Qualquer número impar módulo de 2 é 1 e 1 em Python é True
impares = [numero for numero in numeros if numero % 2]

print(pares)
print(impares)

# 2
res = [numero * 2 if numero % 2 == 0 else numero / 2 for numero in numeros]
print(res)

'''
# lllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllll

# Listas Alinhadas (Nested Lists)
''' - Algumas linguagens de programação(C/Java) possuem uma estrutura de dados chamadas de arrays:
        - Unidimensionais (Arrays/Vetores);
        - Multidimensionais(Matrizes);

Em Python nós temos as Listas

# Exemplos
listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # Matriz 3x3
print(listas)
print(type(listas))

# Como fazemos para acessar os dados?

print(listas[0][1]) # 2
print(listas[2][1]) # 8

# Iterando com Loops em uma lista aninhada
for lista in listas:
    for numero in lista:
        print(numero)

listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]# Matriz 3x3


# List Comprehention

[[print(valor) for valor in lista] for lista in listas]

# Outros Exemplos
# Gerando um tabuleiro/ matix 3x3

tabuleiro = [[numero for numero in range(1, 4)]for valor in range(1, 4)]
print(tabuleiro)

# Gerando jogadas para o jogo da velha
velha = [['x' if numero % 2 == 0 else '0'for numero in range(1, 4)] for valor in range(1,4)]
print(velha)

# Gerando valores inicias

print([['*' for i in range(1, 4)] for j in range(1,4)])
'''
