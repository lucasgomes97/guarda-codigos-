# Len, Abs, Sum e Round
'''Len, Abs, Sum e Round
#len(0 -> Reetorna o tamanho, ou seja, o numero de itens de um iterável.
    # exemplo
print(len('Geek University'))
print(len([1, 2, 3, 4, 5, 6]))
print(len((1, 2, 3, 4, 5)))
print(len(range(0, 10)))
# Por debaixo dos panos, quando utilizamos a função len() o Python faz o seguinte:
# Dunder len
print('Geek University'.__len__())

# abs() -> Retorna o valor absoluto de um número inteiro ou real. De forma básica, seria seu valor real sme o sinal.
    # Exemplo Abs

print(abs(-5))
print(abs(5))
print(abs(3.14))
print(abs(-3.14))

# sum() -> Recebe como prâmetro um iterável, podendo receber um valor inicial, e retorna a soma total dos elementos, incluindo o valor inicial
OBS: O valor inicial default = 0

# Exemplo sum
print(sum([1, 2, 3, 4, 5]))

print(sum([1, 2, 3, 4, 5], 5))

print(sum([1.25, 2.22, 3.33, 4.44, 5.58], 5))

print(sum((1, 2, 3, 4, 5), 5))

print(sum({1, 2, 3, 4, 5}, 5))

# round() -> Retorna um número arrendondado para n dígito de precisão após a casa decimal. Se a precisão não for
informada retorna o inteiro masi próximo da entrada.

# Exemplo round()
print(round(10.2))
print(round(10.5))
print(round(10.6))
print(round(1.212121212121, 2))
print(round(1.21999999999, 2)) '''
