# Generators Expression
'''Generatos -> Tuple Comprehension
nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']
print((any([nome[0] == 'C' for nome in nomes])))

# Poderiamos ter feito utilizando Generators
nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']
print(any(nome[0] == 'C' for nome in nomes))

# List Comprehension
res = [nome[0] == 'C' for nome in nomes]
print(type(res))
print(res)
# Genetator
res = (nome[0] == 'C' for nome in nomes)
print(type(res))
print(res)

# Qual é a utilidade da getsizeof()? -> Retorna a quantidade de bytes em memoria do elemento passado como parâmetro
from sys import getsizeof

# Apresenta quantos bytes a linha está ocupando
print(getsizeof('Gek'))
print(getsizeof('University'))
print(getsizeof(9))
print(getsizeof(91))
print(getsizeof(95489665489954))
print(getsizeof(True))

# Gerando uma lista de números com List Comprehension
list_comp = getsizeof([x * 10 for x in range(1000)])

# Gerando uma lista de números com Set Comprehension
Set_comp = getsizeof({x * 10 for x in range(1000)})

# Gerando uma lista de números com Dictionary Comprehension
dic_comp = getsizeof({x * 10 for x in range(1000)})

# Gerando uma lista de números com Generator
gen_comp = getsizeof(x * 10 for x in range(1000))

print('para fazer a mesma tarefa gastamos em memoria:')

print(f'List Comprehension:{list_comp} bytes')
print(f'Set Comprehension:{Set_comp} bytes')
print(f'Dictionary Comprehension:{dic_comp} bytes')
print(f'Generator Expression:{gen_comp} bytes')

# Eu posso iterar no Generator Expression? Sim!

gen = (x * 10 for x in range(1000))
print(gen)
print(type(gen))

for num in gen:
    print(num)

    '''

