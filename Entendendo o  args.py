# Entendendo o *args
'''O *args é um parâmetro, como outro qualuer. Isso significa que você poderá
chamar de qualquer coisa, desde que comece com asterístico.
Exemplo:
    *xis
Mas por convenção, utilizamos *args para defini-lo

mas o que é *args?
O parâmetro *args utilizado em uma função, coloca os valores extras informados como
entrada em uma tupla. Então desde já lembre-se que tuplas são imutaveis

# Exemplos


def soma_todos_numeros(num1=1, num2=2, num3=3):
    return num1, num2, num3


print(soma_todos_numeros(4, 6, 9))

# Entendendo o *argas

def soma_todos_valores(nome, sobrenome, *args):
    return sum(args)

print(soma_todos_valores("Lucas", "Gomes"))
print(soma_todos_valores("Lucas", "Gomes", 1))
print(soma_todos_valores("Lucas", "Gomes", 2, 3))
print(soma_todos_valores("Lucas", "Gomes", 2, 3, 4))
print(soma_todos_valores("Lucas", "Gomes", 3, 4, 5, 6))
print(soma_todos_valores("Lucas", "Gomes", 23.4, 12.5))

# Outro exemplo de utilização do args

def verifica_info(*args):
    if 'Geek' in args and 'University' in args:
        return "Bem vindo Geeks"
    return "Eu não tenho cetreza quem é você é ..."

print(verifica_info())
print(verifica_info(1, True, "University", "Geek"))
print(verifica_info(1, 'University', 3.1045))

def soma_todos_valores(*args):
    return sum(args)

print(soma_todos_valores())
print(soma_todos_valores(3, 4, 5, 6))

numeros = [1, 2, 3, 4, 5, 6, 7]
# Desempacotador
print(soma_todos_valores(*numeros)) # O asteristico serve para que informamos ao Python que estamos
# passando como argumento uma coleção de dados . desta forma, ele saberá
# que precisará antes desempacotar estes dados
'''
