'Módulo Collection - Ordered Dict'


"""Em um dicionário a ordem de inserção dos elementos não é garantida.
   dicionario = {'a':1, 'b': 2, 'c':3, 'd':4, 'e':5}
for chave,valor in dicionario.items():
    print(f'chave={chave}:valor={valor}')
    
# OrderedDict -> É um dicionário, que nos garante a ordem de inserção dos elementos
# from collections import OrderedDict
# dicionario = OrderedDict({'a':1, 'b': 2, 'c':3, 'd':4, 'e':5})
# for chave, valor in dicionario.items():
#     print(f'chave={chave}:valor={valor}')
# Entendendo a diferença entre Dict e Ordered Dict 
Dicionários comums 
dicionario1 = {'a':1, 'b': 2, 'c':3, 'd':4, 'e':5}
dicionario2 = {'a':1, 'b': 2, 'c':3, 'd':4, 'e':5}
print(dicionario1 == dicionario2) #True/False??? True já que as ordens dos elementos não importa para os dicionários 

from collections import OrderedDict
#Ordered Dict
dicionario1 = OrderedDict({'a':1, 'b': 1, 'c':3, 'd':4, 'e':5})
dicionario2 = OrderedDict({'a':2, 'b': 2, 'c':3, 'd':4, 'e':5})
print(dicionario1 == dicionario2) #True/False??? False já que a ordem dos elementos importa para o Ordered Dict
"""
