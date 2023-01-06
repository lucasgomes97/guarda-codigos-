#PEP8***

"""PEP8- Python Enchancement proposal  ( São propostas de melhoria para linguagem Python)
The zen of Python
import this
A ideia da PEP8 é que possamos escrever códigos Python de forma Pythonica
(1) - Utilize Camel Case para nomes de classes;
(2) - Utilize nomes em minúsculo separados por underline para funções ou variáveis
(3) - Utilize 4 espaços para identação!!! (Não usar TAB)
(4) - Linhas em Branco:
    ( Separar funções e definições de classes com duas linhas em branco:
    Métodos dentro de uma classe devem ser separados com um úbica linha em branco)
(5) - Imports devem ser sempre em linhas separadas:
    ( Imports devem ser colocados no topo do arquivo, logo depois de qualquer comenttários ou docstrings
    e  antes de constantes ou variáveis globais)
(6) - Não deixe espaços em expressões e isntruções
(7) - Termine sempre uma instrução com uma nova linha
"""

#llllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllll


#Dir e Help (Utilitários Python para auxiliar na programação)
"""
Dir -> Apresenta todos os atributos e funções/métodos disponíveis para determinado tipo de dados ou variáveis
ex: dir(tipo de dado/variável)
Help -> Apresenta a documentação/como utilizar os atributos/propriedades  e funções métodos diponiveis para determinado tipo de dado ou variável.
ex: help(descreve a função do comando utilizado) 
"""

#llllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllll

# Recebendo dados do usuário
#entrada de dados
"""print("qual seu nome?")
nome = input()    #-> entrada
# Exemplo de print antigo 
print('seja bem-vindo %s' %nome)
print('Qual sua idade?')
idade = input()

#precessamento

#Saída
#Exemplo de print antigo 
print('seja bem-vindo %s' % nome)
print('O/A tem %s anos' % nome, idade)"""

#Tipo Float
"""
Conhecido como tipo real, decimal(cassa decimais)
OBS: o separador de casas decimais na programação é o ponto e não a virgula.
"""
#tipo Booleano
""" Vem da Algebra Booleana, criada por George Boole
2 constantes, verdadeiro e falso 
True -> Verdadeiro
Falde -> Falso 
OBS: sempre maiúsculo as iniciais 
"""
#Tipo String
""" Em python um dado é considerado do tipo string é considerado do tipo string sempre que:
 - Estiver entre aspas simples -> 'uma string', '234', 'a', 'True', '42.3'
 - Estiver entre aspas duplas  -> "uma string", "234", "a", "True", "42.3"
 - Estiver entre aspas simples triplas -> '''uma string''', '''234''', '''a''', '''True''', '''42.3'''
 - Estiver entre aspas duplas triplas ->
"""
#Escopo de variáveis
""" Dois casos de escopo:
1- Variáveis Globais:
    - Variaveis globais são reconhecidas, ou seja seu escopo compreende todo o progrma
2- Variáveis locais:
    - Variaveis locais são reconhecidas apenas no bloco onde forma declaradas, 
    ou seja, seu escopo esta limitado ao bloco onde foi declarada.
    
Para declarar variáveis em Python fazemos: 
nome_da_variavel = Valor_da_variavel

Python é uma linguagem de tipagem dinâmica. isso significa que ao declararmos 
uma variavel, não colocamos o tipo de dado dela.
Este tipo é inferido ao atribuírmos o valor a mesma.

Exemplo em C:
int numero = 42: 

exemplo em Java:
int numero =43;
"""
#llllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllll

# listas 
"""
listas em Python funcional como vetores/matrizes (arrays) em outras linguagens, com a diferença de serem DINAMICO e também de podermos colocar QUALQUER tipo de dado.

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
# Isso em Python é chamado de Shallow Copy.

"""
# Tuplas ( Tuple)
'''
Tuplas são bastantes parecidas com listas.

Existem basicamente duas diferenças basicas:

1- As tuplas são representadas por parênteses ()

2- As tuplas são imutáveis : Isso significa ao se criar uma tupla ela não muda. 
Toda operação em uma tupla gera uma nova tupla 

#Cuidado 1 : As tuplas são reprensentadas por (), mas veja:
    tupla1 = (1, 2, 3, 4, 5, 6)
    print(type(tupla1))

    tupla2 = 1, 2, 3, 4, 5, 6
    print(tupla2)
    print(type(tupla2))

# Cuidaddo 2 : Tuplas com 1 elemento:
    tupla3= (4)  Isso não é uma tupla!!
    print(tupla3)
    print(type(tupla3)) 

    tupla4 = (4,) Isso é uma tupla 
    print(tupla4)
    print(type(tupla4))

#Conclusão : Podemos concluir que tuplas são definidas pela vírgula e não pelo uso de parenteses ()
(4)_>Isso não é uma tupla!!
(4,)->Isso é uma tupla 
4, ->Isso é uma tupla 

# Podemos gerar um tupla  dinamicamente com um range(início,fim,passo)
tupla = tuple(range(11))
print(tupla)
print(type(tupla))

# Desempacotamento de tupla 
tupla = ("Geek University", 'Programação em Python essencial')
escola, curso = tupla 
print(escola)
print(curso)
# OBS : Gera errp (ValueError) se colocarmos um número diferente de elementos para desempacotar 

# Métodos para: adição e remoção de elementos nas tuplas não existem, dado o fato das tuplas serem imutaveis.
# soma*, Valor Máximo*, Valor Mínimo* e tamanho
#*Se os valores forem todos inteiros ou reais 

tupla = (1, 2, 3, 4, 5, 6)
print(sum(tupla)) 
print(max(tupla))
print(min(tupla))
print(len(tupla))

# Concatenação de tuplas (Juntar)

tupla1 = (1, 2, 3)
print(tupla1)

tupla2 = (4, 5, 6)
print(tupla2)

print(tupla1 + tupla2) # Tuplas são imutáveis 

print(tupla1)
print(tupla2)

tupla3 = tupla1 + tupla2 # Tuplas são imutaveis, mas podemos sobrescrever seus valores 

print(tupla3)
'''
# Tipo none:
#     O tipo none em Python representa o tipo sem tipo ou poderia ser conhecido tambem
# como tipo vazio, porém, falar que é um tipo sem tipo é masi apropriado.
'''Certo = None
Errado = none 
Quando utilizamos?
    Podemos utilizar o None quando queremos criar uma variavel e inicializar com um tipo sem tipo, 
    antes de recerbemos um valor final.
    OBS: O tipo None em Python é considerado sempre Falso'''
#Dicionários 
""" OBS: em algumas linguagens de programção, os dicionários Python são conhecidos por mapas.
Dicionários são coleções ddo tipo chave/valor.

Dicionários são representados por chaves {}
    print(type({}))

OBS: Sobre dicionários:
    - Chaves e valor são separados por dois pontos 'chave valor':
    - Tanto chave quanto valor pode ser de qualquer tipo de dados:
    - podemos misturar tipos de dados:?

# Criação de dicionários    
# Forma 1 (mais comum)
paises = {'br':'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
print(paises)
print(type(paises))

# forma 2(menos comum)=
paises1= dict(br ='brasil', eua='Estados unidos', py='Paraguay')
print(paises1)  
print(type(paises1))

# Acessando elementos 
# Forma 1 - acessando via chave, da mesma forma que lista/tupla
print(paises['br'])
print(paises["eua"])

# OBS: Caso tentarmos fazer um acesso a uma chave que não existe teremos o erro  KeyError

#Forma 2 - Acessando via get - Recomendada !!!
print(paises.get('br'))
print(paises.get("ru"))

Ex: Caso o get não encontrar o objeto com a chave informada será retornado o valor none e não um erro 
    pais = paises.get('py', "Não encontrado")

        if pais:
            print(f"encontrei o pais {pais} ")
    else:
        print(f"não encontrei o pais{pais}")


EX2: Podemos definir um valor padrão para caso não encontrarmos o objeto com a chave informada 
    paises = {'br':'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

    pais = paises.get('ru', "Não encontrado")

    print(f"encontrei o pais {pais} ")  

 # Podemos Verificar se determinada chave se encontra em um dicionário
print('br'in paises)
print("ru" in paises)
print("Estados Unidos" in paises)
if "ru" in paises:
    russia = paises['ru']

# Podemos utilizar qualquer tipo de dado inclusive ( int, float, string, boolean), inclusive lista, tupla dicionário, como chaves.
#de dicionarios
# Tuplas por exemplo são bastantes interessantes de serem utilizadas como chaves de dicionarios,
pois as mesmas são imutaveis
localidade = {
    (35.6895, 39.6917):'Escritório em Tókyo',
    (40.7128, 74.0060): "Escritório em Nova York",
    (37.7749, 122.4194): "Escritório em São Paulo",
}
print(localidade)
print(type(localidade))

#Adicionar elementos em um dicionário

receita = {'jan': 100, 'fev': 120, 'mar': 300}
print(receita)
#Forma 1 mais comum !!!!!
receita ['abr'] = 350
print(receita)

#Forma 2
novo_dado = {'mai': 500}
receita.update(novo_dado)   #  ou receita.update({'mai': 500})
print(receita)
# atualizando dados em um dicionário
#Forma 1 
receita['mai'] = 540
print(receita)

# Forma 2 
receita.update({'mai': 600})
print(receita)

#Conclusão:
     1-A forma de adicionar novos elementos ou atulizar dados em um dicionário é a mesma.
     2- Em dicionários, NÃO PODEMOS TER CHAVES REPETIDAS.


#Conclusão:
     1-A forma de adicionar novos elementos ou atulizar dados em um dicionário é a mesma.
     2- Em dicionários, NÃO PODEMOS TER CHAVES REPETIDAS.

# Remover dados de um dicionário
receita = {'jan': 100, 'fev': 120, 'mar': 300}
print(receita)

#Forma 1 Mais comum !!!!
ret = receita.pop('mar')
print(ret)
print(receita)
# OBS:aqui precisamos sempre informar a chave e caso não localize o elemento um KeyError é informado 
#OBS2: ao remover um objeto, o valor deste objeto é sempre retornado.

#Forma 2 neste caso o calor removido não é retornado 

del receita['fev']
print(receita)

del receita['fev'] # Se achave não existir será gerado um keyError


    """

# Imagine que vc tem um e-comerce onde temos um carrinho de compras na qual adicionamos produtos.
'''
Carrinhos de compras:
    Produto 1:
        -nome:
        -quantidade:
        -preço:
    Produto 2:
        -nome:
        -quantidade:
        -preço:      

# 1 - Pderiamos utilizar uma lista para isso? sim
carrinho = []
produto1= ['Play 4 ', 1, 230.00]
produto2= ['god of war ', 1, 130.00]

carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)  #OBS: teriamos que saber qual indice de cada produto 

# 2 - Pderiamos utilizar uma tupla para isso? sim

produto1= ('Play 4', 1, 2300.00)
produto2 =("god of war 4", 1, 150.00)
carrinho =(produto1+produto2)
print(carrinho)  #OBS: teriamos que saber qual indice de cada produto

# 3- Pderiamos utilizar um dicionario para isso? sim

produto1 = {'nome': "play4", 'quantidade':1, 'preço':2300}
produto2 = {'nome': "god of war", 'quantidade':1, 'preço':130}

carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)
# desta forma, facilmente adicionamos ou removemos produtos no carrinho e em cadaproduto
#Podemos ter a certeza sobre cada informação  

'''
