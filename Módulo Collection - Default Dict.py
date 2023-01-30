# Módulo Collection - Default Dict
'''dicionario = {'curso': 'Programação em Python'}
print(dicionario)
print(dicionario['curso'])

Default Dict -> Ao criar um dicionário utilizando-o, nos informamos um valor default,
podendo utilizar um lambda para isso. Este valor será utilizado sempre que não houver
um valor definido, Caso tentamos acessar uma chave que não existe, essa chave será
criada e o valor default será atribuido.

OBS: Lambdas são funções sem nome, que podem ou não receber parametros de entradas e retornar valores

from collections import defaultdict
dicionario = defaultdict(lambda: 0)
dicionario['curso'] = 'Programação em Python'
print(dicionario['outro']) # KeyError no dicionário comum, mas aqui não
print(dicionario)'''
