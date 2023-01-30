# listas
""" listas em Python funcional como vetores/matrizes (arrays) em outras linguagens, com a diferença de serem DINAMICO e também de podermos colocar QUALQUER tipo de dado.

Linguagens C/Java: Arrays:
    - Possuem tamanho e tipo de dado fixo:
        Ou seja, nestas linguagens se você criar um array do tipo int e com tamanho 5, este array será SEMPRE do tipo inteiro e poderá ter SEMPRE no máximo 5 valores.
    - Já em Python:

    - Dinámico: Não possuem tamanho fixo: ou seja, podemos criar a lista e simplismente ir adicionando elementos;
    - Qualquer tipo de dados: As listas não possuem tipo de dado fixo; Ou seja , podemos  colocar qualquer tipo de dado:
As listas em Python são representadas por colchetes: []
Listas são mutaveis, ou seja pode mudar constantemente

type ([])
lista1 =  [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]
lista2 = ['G', 'e', 'e','k','','U','n','i','v','e', 'r','s','i','t','y']
lista3 = []
lista4 =  list(range(11))
lista5 = list("Geek University")

Podemos facilmente checar se determinado valor está contido na lista
if 8 in lista4:
    print("Encontrei o Número 8")
else:
    print("não encontrei o número 8")

num = 7
if num in lista4:
    print(f"Encontrei o número{num}")
else:
    print(f"não encontrei o número {num}")

# Podemos facilmente ordenar uma lista

lista1.sort()
print(lista1)

# Podemos facilmente contar o Número de ocorrências de um valor em uma lista
print(lista1.count(1))
print(lista5.count("e"))

#adicionar elementos em listas


#Para adicionar elementos/valores em listas, utilizamos aa função append


print(lista1)
lista1.append(99)
print(lista1)
#OBS: Com append, nós só conseguimos adicionar um elemento por vez
#lista1.append(12,22,56) #vai dar erro

lista1.append([8, 3, 1]) # Coloca a lista como elemento único(sublista)
print(lista1)

if [8, 3, 1] in lista1:
    print("Encontrei a lista")
else:
    print("Não encontrei a lista")

lista1.extend([123,44,67]) # Coloca cada elemento da lista como valor adicional á lista
print(lista1)

# Podemos inserir um novo elemento na lista informando a posição do índice
#OBS: Isso não substitui o valor inicial o mesmo será deslocado para a direita da lista.
lista1.insert(2,"Novo valor")
print(lista1)
#Podemos facilmente juntar duas listas
lista6 = lista1 + lista2
print(lista6)

# Podemos facilmente inverter uma lista
#Forma1
lista1.reverse()
lista2.reverse()
print(lista1)
print(lista2)
#Forma 2
print(lista1[::-1])
print(lista2[::-1])

#copiar uma lsta
lista6 = lista2.copy()
print(lista6)

#Podemos contar quantos elementos existem dentro da lista
print(len(lista1))

# Podemos remover facilmente o último elemento de uma lisa
#OBS: o pop não somente remove o último elemento mas também o retorna
print(lista5)
lista5.pop()
print(lista5)

# Podemos remover um elemento pelo índice
# OBS: Os elementos a direita deste índice serão deslocados para a esquerda.
lista5.pop(2)
print(lista5)

# Podemos remover todos os elementos, ou seja, zerar toda a lista
print(lista5)
lista5.clear()
print(lista5)

# Podemos facilmente repetir elementos em uma lista

nova = [1, 2, 3]
print(nova)
nova = nova *3
print(nova)

# Podemos facilmente converter uma string para uma lista.
#EX1:
curso = "Programação em Python Essencial"
print(curso)
curso = curso.split()
print(curso )
# OBS: Por padrão, o split separa os elementos da lista pelo espaço entre elas .
#EX2:
curso = "Programação,em,Python,Essencial"
print(curso)
curso= curso.split(",")
print(curso)

lista6 = ['Programação', 'em', 'Python', 'Essencial']

print(lista6)
#OBS: Abaixo estamos falando: pega a lista 6, coloca espaço entre cada elemento e trasnforma em uma string
curso = ' ' .join(lista6)
print(curso)
#OBS: Abaixo estamos falando: pega a lista 6, coloca o cifrão ($) entre cada elemento e trasnforma em uma string
curso = '$' .join(lista6)
print(curso)

#Podemos realmente colocara qualquer tipo de dado em uma lista, inclusive esses dados
lista6 = [1, 2.34, True, 'geek', 'd', [1, 2, 3], 4568754874]

# Interando sobre Listas
#Ex:1 - Utilizando For
soma = 0
for elemento in lista1:
    print(elemento)
    soma= soma + elemento
print (soma)

#EX2: Utilizando while
carrinho = []
produto = ''

while produto != "sair":
    print("Adicione um produto na lista ou digite 'sair' para sair:")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)

# Utilizando variáveis em listas
numeros = [1, 2, 3, 4, 5]
num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5

numeros[num1, num2, num3, num4, num5]
print(numeros )

# Em listas fazemos acesso de forma indexada

#          0         1         2       3
cores = ['verde','anarelo', 'azul', 'branco']
print(cores[0])  #verde
print(cores[1])  #amarlo
print(cores[2])  #azul
print(cores[3])  #branco

# Em listas fazemos acesso de forma indexada

#          0         1         2       3
cores = ['verde','anarelo', 'azul', 'branco']
print(cores[0])  #verde
print(cores[1])  #amarlo
print(cores[2])  #azul
print(cores[3])  #branco

# Fazendo acesso aos elementos de forma indexada inversa
# Para entender o índice negativo, pense na lista como um círculo, onde
#o final de um elemento está ligado ao início da lista
print(cores[-1]) #branco
print(cores[-2]) #azul
print(cores[-3]) #amarlo
print(cores[-4]) #verde
#print(cores[-5]) # Erro, pois não existe indice -5


for cor in cores:
    print(cor)

indice = 0
while  indice < len(cores):
    print(cores[indice])
    indice = indice + 1


# em lista grandes gerar indices em um for
for indice, cor in enumerate(cores):
    print(indice, cor)

# Listas aceitam valores repetidos
lista= []
lista.append(42)
lista.append(42)
lista.append(33)
lista.append(33)
lista.append(32)

# Outros métodos nã tão importantes mas também úteis
#Encontrar o índice de um elemento na lista
numeros = [5, 6, 7, 5, 8, 9, 10]

#em qual iíndice da lista está o valor 6?
print(numeros.index(6))

#em qual iíndice da lista está o valor 9?
print(numeros.index(9))
# OBS: Caso nã o tenha este elemento na lista, será apresentado erro ValueError

print(numeros.index(5)) #retorna o primeiro elemento  encontrado

#Podemos fazer uma busca dentro de um range, ou seja, qual indice começar a buscar
print(numeros.index(5, 1))#buscando a partir do índice 1
print(numeros.index(5, 2))#buscando a partir do índice 2
print(numeros.index(5, 3))#buscando a partir do índice 3
#print(numeros.index(5, 4))#buscando a partir do índice 4
#OBS: Caso nã o tenha este elemento na lista, será apresentado erro  ValueError

# Podemos  fazer busca dentro de um range , início/fim
print(numeros.index(8, 3, 6)) #Buscar  o indice do valor 8, entre os índices 3 e 6

# Revisão do slicing

#lista[inicio:fim:passo]
#range(inicio:fim:passo)

# Trabalhando com slice de lista com o parâmetro 'inicio'

lista = [1, 2, 3, 4]

print(lista[1:])#iniciando no índice 1 e pegando todos os elementos restantes

# Trabalhando com slice de lista com o parâmetro 'Fim'

print(lista[:2]) # Começa em 0, pega até o índice 2-1

print(lista[:4]) # Começa em 0, pega até o índice 4-1

print(lista[1:3]) # Começa em 1, pega até o índice 3-1

print(lista[:-1])


# Trabalhando com slice de lista com o parâmetro 'Passo'

print(lista[1::2]) #Começa em 1, e vai até o final de 2 em 2

print(lista[::2]) #Começa em 0, e vai até o final de 2 em 2

print(lista[1::-1])

#Invertendo valores em uma lista

nomes = ['geek','university']
nomes[0], nomes[1], nomes[0]
print(nomes)

nomes = ['geek','university']
nomes.reverse()
print(nomes)

#Soma*, procurar valor máximo*, valor mínimo*, tamanho


# * se os valores forem todos inteiros ou reais .
lista  = [1, 2, 3, 4, 5, 6]
print(sum(lista)) #soma
print(max(lista)) #máximo valor
print(min(lista)) #minimo valor
print(len(lista)) #Tamanho da lista

#transformar uma lista em tupla

lista  = [1, 2, 3, 4, 5, 6]
print(lista)
print(type(lista))

tupla= tuple(lista)
print(tupla)

# Desempacotamento de listas
lista = [1, 2, 3]
num1, num2, num3 = lista
print(num1)
print(num2)
print(num3)

#OBS : Se tivermos um número diferente de elementos na lista ou variaveis  para receber os dados  teremos ValueError

# Copiando uma lista para outra  (Shallow Copy e Deep Copy)
#Forma 1
lista = [ 1,2,3]
print(lista)

nova = lista.copy() #cópia
print(nova)
nova.append(4)
print(lista)
print(nova)
#Veja que ao utilzarmos lista.copy(), copiamos os dados da lista para uma nova lista, mas elas
#ficaram totalmente independentes, ou seja, modificando uma lista, não afeta a outra. Isso em Python
#é chamado de Deep copy ( copia profunda)

#Forma 2 - Shallow copy

lista = [ 1,2,3]
print(lista)

nova = lista  #cópia
print(nova)
nova.append(4)
print(lista)
print(nova)

# OBS: veja que utilizamos a cópia via atribuição e copiamos os dados da lista para a nova lista, mas
#após realizar modificação em uma das listas, essa modificação se refletiu em ambas as listas.
# Isso em Python é chamado de Shallow Copy."""
