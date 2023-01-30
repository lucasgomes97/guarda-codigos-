# Módulo Collection - Counter (Contador)
'''
Collentions -> High performance Container Datetypes
Counter -> Recebe um interavel como parametro e cria um objeto do tipo Colection Counter que é parecido
com um dicionário, contendo como chave o elemento da lista passada como paremetro e como valor a quantidade
de ocorrências desse elemento.

#Utilizando o counter

from collections import Counter

#Exemplo 1
# Podemos utilizar qualquer interavel . neste exemplo foi uma lista
lista = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 30, 45, 50]
#Utilizando o Counter
res = Counter(lista)
print(type(res))
print(res)
#Counter({1: 3, 2: 3, 3: 3, 4: 3, 5: 3, 30: 1, 45: 1, 50: 1})
# Veja que para cada elemento da lista o conter criou uma chave e colocou como valor a quantidade de ocorrências.

# Exemplo 2
print(Counter('Geek University'))

texto = Python é uma linguagem de programação de alto nível,[5] interpretada de script, imperativa, orientada a objetos,
funcional, de tipagem dinâmica e forte.
Foi lançada por Guido van Rossum em 1991.[1] Atualmente, possui um modelo de desenvolvimento comunitário,
aberto e gerenciado pela organização sem fins lucrativos Python Software Foundation.
Apesar de várias partes da linguagem possuírem padrões e especificações formais, a linguagem, como um todo,
não é formalmente especificada.
O padrão na pratica é a implementação CPython.
palavras = texto.split()
#print(palavras)
res = Counter(palavras)
print(res)
#Encontrado as 5 palavras com mais ocorrencias no texto
print(res.most_common(5))'''
