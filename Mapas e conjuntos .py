# Mapas -> Conhecidos em Python como dicionários
# Interar sobre dicionérios
'''#Imprimindo a chaves
for chave in receita:
    print(chave)
#Imprimindo os valores
for chave in receita:
    print(receita[chave])

for chave in receita:
    print(f'{chave} recebi R$ {receita[chave]}')'''

# llllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllll

# Conjuntos
''' Conjuntos em qualquer linguagem de programação, estamos fazendo referência a teoria dos conjuntosda matemática.
- Aqui no Python os conjuntos são chamados de sets.
Dito ista, na mesma forma que na matemática:
    Sets (conjuntos) não possuem valores duplicados;
    Sets (conjuntos) não possuem valores ordenados;
    Elementos nãs sãp acessados via índice, ou seja, conjuntos não são indexados;

Conjuntos são bons para se utilizar quando precisamos armazenar elementos
mas não nos importamos com a ordenação deles. quando não precisamos se preocupar
com chave, valores e itens duplicados.
Os conjuntos (sets) são referencias em Python com chaves{}
    Diferença entre conjuntos (SETS) e Mapas (Dicionários em Python;
        - Um dicionario tem chave/valor;
        - um conjunto tem apenas valor;
        
#Definindo um Conjunto
#Forma 1
s = set({1, 2, 3, 4, 5, 6, 7, 2, 3}) #repare que temos valores repitidos
print(s)
print(type(s))
#OBS: Ao criar um conjunto, caso seja adicionado um valor já existente, o mesmo
#será ignorado sem gerar error ee não fará parte do conjunto

#Forma2 -Mais comum
s = {1, 2, 3, 4, 5, 6, 7, 2, 3}
print(s)
print(type(s))

if 3 in s:
    print('Tem o 3')
else:
    print('não tem o 3')
    
# Importante lembras que, além de não termos valores duplicados, não temos ordem

# Listas aceitam valores duplicados, então temos 10 elementos
lista = [99, 2, 34, 23, 2, 34, 12, 1, 44, 5]
print(f'lista:{lista} com{len(lista)} elementos')
# Listas aceitam valores duplicados, então temos 10 elementos
tupla = (99, 2, 34, 23, 2, 34, 12, 1, 44, 5)
print(f'Tupla:{tupla} com{len(tupla)}')
# Listas não aceitam valores duplicados, então temos 8 elementos
dicionario = {}.fromkeys(lista, 'dict')
print(f'Dicionario; {dicionario} com{len(dicionario)}')
# Listas não aceitam valores duplicados, então temos 8 elementos
conjunto = {99, 2, 34, 23, 2, 34, 12, 1, 44, 5}
print(f'Conjunto:{conjunto} com{len(conjunto)}')

# Assim como todo outro conjunto Python podemos colocar tipos de dados misturados em Sets

s = {1, 'b', True, 34.22, 44}
print(s)
print(type(s))

#Podemos iterar em um set normalmente
for valor in s:
    print(valor)

# Uso interessantes com sets
# Imagine que fizemos um formulário de cadastro de vizitantes em uma feira ou museu, e os visitantes
#informam manualmente a cidade de onde vieram.

# Nós adicionamos cada cidade em uma lista Python, já que em uma lista podemos adicionar novos elementos e ter repetição

cidades = ['belo horizonte', 'Sao paulo', 'Campo Grande', 'Cuiaba', 'Campo Grande', 'Sao paulo', 'Cuiaba']
print(cidades)
print(type(cidades))

# Agora precisamos saber quantas cidades distintas, ou seja, únicas, temos.
# O que você faria? faria um loop na lista ?
#Podemos utilizar o set para isso:

print(len(set(cidades)))

# Adicionando elementos em um conjunto
s = {1, 2, 3}
print(s)
s.add(4)
s.add(4) # duplicidade não gera error. Simplismente não é adicionado 
print(s)

# Remover elementos em um conjunto
s = {1, 2, 3}
print(s)

# Forma 1
s.remove(3)  # Não é indice, informamos o valor a ser removido
print(s)
# OBS: caso o valor não seja encontrado será gerado o erro KeyError. Nenhum valor é retornado 

# Forma 2
s.discard(2)
s.discard(2) # OBS: Se o valor não for encontrado, nenhum erro é gerado
print(s)

# Copiando um conjunto para outro...
s = {1, 2, 3}
print(s)

# Forma 1 - Deep Copy
novo = s.copy()
print(novo)
novo.add(4)
print(novo)
print(s)

# Forma 2 - Shallow Copy
novo = s
novo.add(4)
print(novo)
print(s)

# Podemos remover todos os itens de um conjunto
s.clear()
print(s)


# Métodos matemáticos de um conjunto

# Imagie que temos 2 conjuntos:  um contendo estudantes de python e outro contendo estudantes de Java

estudantes_Python = {'Marcos', 'Patricia', 'Pedro', 'Julia', 'Guilherme'}
estudantes_Java = {'Fernando','Gustavo', 'Julia', 'Ana', 'Patricia'}

# Veja que temos que alguns alunos estudantes de Python também estudam Java.
# precisamos gerar um conjunto com nomes de estudantes únicos.
# Forma 1 - utilizando union
unicos1 = estudantes_Python.union(estudantes_Java)
print(unicos1)

unicos1 = estudantes_Java.union(estudantes_Python)
print(unicos1)

#Forma 2 - utilizando o caractere pipe [image]

unicos2 = estudantes_Java | estudantes_Python
print(unicos2)

# Gerar um conjunto de estudantes que estão em ambos  os cursos

#forma ' - Utilizando intersection

ambos1 = estudantes_Python.intersection(estudantes_Java)
print(ambos1)

# Forma 2 Utilizando  o &

ambos2 = estudantes_Python & estudantes_Java
print(ambos2)

# Geara um conjunto de um curso que não estão no outro

so_python = estudantes_Python.difference(estudantes_Java)
print(so_python)

so_java = estudantes_Java.difference((estudantes_Python))
print(so_java)

# Soma* , valor maximo*, valor minimo*, tamanho ( * se os valores forem inteiros ou reais)

s = {1, 2, 3, 4, 5, 6}
print(sum(s))
print(max(s))
print(min(s))
print(len(s))
'''
