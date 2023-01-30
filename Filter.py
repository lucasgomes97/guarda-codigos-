# Filter
''' filter()-> Serve para filtrar dados de uma determinada coleção.

valores = 1, 2, 3, 4, 5, 6
medeia = (sum(valores) / len(valores))
print(medeia)

import statistics
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]
# calculando a media dos dados utilizando a função mean()

media = statistics.mean(dados)
print(media)
# OBS : Assim como a função Map(), a filter() recebe dois parâmetros, sendo uma função e um iterável
res = filter(lambda x: x >= media, dados)
print(list(res))
print(f'Novamente: {list(res)}')
# OBS: Assim como a função Map(), após serem utilizados os dados de filter() eles são excluidos da memória

paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Venezuela']
# res = filter(lambda pais: len(pais) > 0, paises)
# res = filter(None, paises)
res = filter(lambda pais: pais != '', paises)
print(list(res))

# A diferença entre map() e filter() é:
# map() -> REcebe dois parãmetros, uma função e um iterável e retorna um objeto mapeando a função para cada elemento do  iterável:
# filter() -> Recebe dois parãmetros, uma função e um iterável e retorna um objeto filtrando apenas os elementos de acordo com a função

# Exemplo mais completo
usuarios = [
    {'Username': "samuel", 'tweets': ["eu adoro bolos", "Eu adoro pizzas"]},
    {'Username': "carla", 'tweets': ["eu adoro gatos"]},
    {'Username': "jeff", 'tweets': []},
    {'Username': "bob123", 'tweets': []},
    {'Username': "doggo", 'tweets': ["eu adoro cachorros", "Eu vou sair hoje"]},
    {'Username': "gal", 'tweets': []},
]
print(usuarios)

# Filtrar os usuarios que estão inativos no Twitter
# Forma 1
#inativos = list(filter(lambda usuario: len(usuario['tweets']) == 0, usuarios))

# Forma 2
inativos = list(filter(lambda usuario: not (usuario['tweets']), usuarios))
print(inativos)

# Combinar filter() e map()
nomes = ["vanessa", "Ana", "Maria"]

# Devemos criar uma lista contendo "Sua instrutura é + nome, desde que cada nome tenha menos de 5 caracteres

lista = list(map(lambda nome: f'sua instrutora é {nome}', filter(lambda nome: len(nome) < 5, nomes)))
print(lista)'''
