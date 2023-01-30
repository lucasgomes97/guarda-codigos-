# Módulo Collection -> Named Tuple
'''
tupla = (1, 2, 3)
Named Tuple -> São tuplas diferenciadas, onde especificamos um nome para a mesma e também parâmetros.

from collections import namedtuple
# precisamos definir o nome e parametro
#forma1 Declaração da tuple
cachorro = namedtuple('cachorro','idade raça nome')
#forma2 Declaração da tuple
cachorro = namedtuple('cachorro','idade, raça, nome')
#Forma 3 Declaração da tuple
cachorro = namedtuple('cachorro',['idade', 'raça', 'nome'])
# Usando
thor = cachorro(idade=2, raça="pit monster", nome='thor')
print(thor)
print(thor[0]) #idade
print(thor[1]) #raça
print(thor[2]) #nome

# Forma 2
print(thor.idade) #idade
print(thor.raça) #raça
print(thor.nome) #nome

print(thor.index('pit monster'))
print(thor.count('pit monster')) '''
