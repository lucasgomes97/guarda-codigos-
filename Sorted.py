# Sorted
''' Obs: Não confunda com a função sorte que já estudamos em listas . o sort()
só funciona em listas

Podemos utilizar o sorted() com qualquer iterável.
Como o próprio nome diz, sorted() serve para ordenar.
OBS : O sorted sempre retorna uma lista com os elementos d iterável ordenados

# Exemplo
numeros = (6, 1, 8, 2)
print(numeros)

print(sorted(numeros)) # Ordenar do menor para o maior

print(numeros)

# Adicionando parãmetros ao sorted()

numeros = [6, 1, 8, 2]
print(numeros)
print(sorted(numeros))

print(sorted(numeros, reverse=True)) # ordena do maior para o menor


# Podemos utilizar o sorted para coisas mais complexas

usuarios = [
    {'Username': "samuel", 'tweets': ["eu adoro bolos", "Eu adoro pizzas"]},
    {'Username': "carla", 'tweets': ["eu adoro gatos"]},
    {'Username': "jeff", 'tweets': []},
    {'Username': "bob123", 'tweets': [], "cor": "amarelo"},
    {'Username': "doggo", 'tweets': ["eu adoro cachorros", "Eu vou sair hoje"]},
    {'Username': "gal", 'tweets': [], "cor":"preto", "musica": "rock"},
]

print(usuarios)
# Ordenando por Username - Ordem alfabética
print(sorted(usuarios, key=lambda usuario: usuario["Username"]))
# Ordenando por tweets - Ordem crescente
print(sorted(usuarios, key=lambda usuario: usuario["tweets"]))
# Ordenando por Username - Ordem alfabética reversa
print(sorted(usuarios, key=lambda usuario: usuario["Username"], reverse=True))

# exemplo
musicas = [
    {'titulo': "Thundertruck", "tocou": 3},
    {'titulo': "xurastei", "tocou": 3},
    {'titulo': "cabeça de gelo ", "tocou": 10},
    {'titulo': "eu voltei", "tocou": 5},
]
# Ordena da menos tocada para a mais tocada
print(sorted(musicas, key=lambda musica: musica['tocou']))

# Ordena da mais tocada para a menos tocada
print(sorted(musicas, key=lambda musica: musica['tocou'], reverse=True))
'''
