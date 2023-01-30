# **Kwargs
'''poderiamos chamar este parametro de **xis, mas por convenção chamamos por **Kwargs.
Este é só mais um parâmetor, mas diferente do *args que coloca os valores extras
em uma tupla, o **Kargs exige que utilizemos parãmetros nomeados, e trasnforma esses
parâmetros extrs em um dicionário.

def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é {cor}')

cores_favoritas(marcos= 'verde', julia='amarelo',fernanda='azul', vanessa='branco')

# OBS: Os parâmetros *args e **Kargs não são obrigatórios.
cores_favoritas()
cores_favoritas(geek='navy')

# Exemplo mais complexo
def cumprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'Python':
        return 'você recebeu um comprimento Pythõnico Geek'
    elif 'geek'in kwargs:
        return f"{kwargs['geek']} Geek"
    return 'Não tenho certeza quem é você é...'

print(cumprimento_especial())
print(cumprimento_especial(geek='Python'))
print(cumprimento_especial(geek='oi'))
print(cumprimento_especial(geek='especial'))

# Nas nossas funções, podemos ter (NESTA ORDEM)
-parametos obrigatórios ;
-*args
- parametos default(não obrigatorios)
- **Kwargs

def minha_funcao(idade, nome, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade}anos')
    print(args)
    if solteiro:
        print('Solteiro')
    else:
        print('Casado')
    print(kwargs)


minha_funcao(8, 'julia')
minha_funcao(18, 'felicity', 4, 5, 3, solteiro=True)
minha_funcao(34, 'Felipe', eu='não', voce='vai')
minha_funcao(19, 'carla', 9, 4, 3, java=False, python=True)

# Entendendo por qu~e é importante manter a ordem dos parâmetros da declaração

# Função com a ordem correta de parâmetors

def mostra_info(a, b, *args, instutor='Geek', **kwargs):
    return [a, b, args, instutor, kwargs]

print(mostra_info(1, 2, 3, sobrenome='University', cargo='Instrutos'))

# Desempacotar com **Kwarg
def mostra_nomes(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"

nomes = {'nome': 'Felicity', 'sobrenome': 'Jones'}
print(mostra_nomes(**nomes))

def soma_multiplos_numeros(a, b, c, **kwargs):
    print(a + b + c)

lista = [1, 2, 3]
tupla = (1, 2, 3)
conjunto = {1, 2, 3}

soma_multiplos_numeros(*lista)
soma_multiplos_numeros(*tupla)
soma_multiplos_numeros(*conjunto)

dicionario = dict(a=1, b=2, c=3)
soma_multiplos_numeros(**dicionario)
# OBS!! Os nomes da chave em um dicionário devem ser os mesmos dos parãmetros da função
dicionario = dict(a=1, b=2, c=3, nome="Geek")
soma_multiplos_numeros(**dicionario, lang='Python')
'''
