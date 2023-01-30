# Min e Max
'''max() -> retorna o  maior valor em um iterável ou o maior de dois ou mais elementos.
    # Exemplo
lista = [1, 8, 45, 698, 898, 2, 333]
print(max(lista))

tupla = (1, 8, 45, 698, 898, 2, 333)
print(max(tupla))

conjunto = {1, 8, 45, 698, 898, 2, 333}
print(max(conjunto))

dict = {'a': 1, 'b': 8, 'c': 45, 'd': 698, 'e': 898, 'f': 2, 'g': 333}
print(max(dict.values()))

# Fassa um programa que receba dois valores do usuário e mostre o maior
val1 = int(input('Informe o primeiro valor: '))
val2 = int(input('Informe o segundo valor: '))
print(max(val1, val2))

# min() -> Retorna o menor valor em um iterável ou o menor de dois  ou mais elementos .

lista = [1, 8, 45, 698, 898, 2, 333]
print(min(lista))

tupla = (1, 8, 45, 698, 898, 2, 333)
print(min(tupla))

conjunto = {1, 8, 45, 698, 898, 2, 333}
print(min(conjunto))

dict = {'a': 1, 'b': 8, 'c': 45, 'd': 698, 'e': 898, 'f': 2, 'g': 333}
print(min(dict.values()))

val1 = int(input('Informe o primeiro valor: '))
val2 = int(input('Informe o segundo valor: '))
print(min(val1, val2))

# Outros exemplos

nomes = ['Arya', 'Samson', 'Dora', 'Tim', 'Ollivander']
print(max(nomes))
print(min(nomes))
print(max(nomes, key=lambda nome: len(nome)))
print(min(nomes, key=lambda nome: len(nome)))

musicas = [
    {'titulo': "Thundertruck", "tocou": 3},
    {'titulo': "xurastei", "tocou": 3},
    {'titulo': "cabeça de gelo ", "tocou": 10},
    {'titulo': "eu voltei", "tocou": 5},
]
print(max(musicas, key=lambda musica: musica['tocou']))
print(min(musicas, key=lambda musica: musica['tocou']))

# Desafio!! Imprima somente o título da música mais e menos tocada
print(max(musicas, key=lambda musica: musica['tocou'])['titulo'])
print(min(musicas, key=lambda musica: musica['tocou'])['titulo'])
# Desafio como encontrar a musica mais e menos tocada sem usar max(), min() e kambda?
max = 0
for musica in musicas:
    if musica['tocou'] > max:
        max = musica['tocou']
for musica in musicas:
    if musica['tocou'] == max:
        print(musica['titulo'])

min = 999999
for musica in musicas:
    if musica['tocou'] < min:
        min = musica['tocou']
for musica in musicas:
    if musica['tocou'] == min:
       print(musica['titulo']) '''
