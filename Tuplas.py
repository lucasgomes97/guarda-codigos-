
# Tuplas ( Tuple)
""" Tuplas são bastantes parecidas com listas.

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

print(tupla3) """

# Tipo none:
#     O tipo none em Python representa o tipo sem tipo ou poderia ser conhecido tambem
# como tipo vazio, porém, falar que é um tipo sem tipo é masi apropriado.
'''Certo = None
Errado = none 
Quando utilizamos?
    Podemos utilizar o None quando queremos criar uma variavel e inicializar com um tipo sem tipo, 
    antes de recerbemos um valor final.
    OBS: O tipo None em Python é considerado sempre Falso'''
