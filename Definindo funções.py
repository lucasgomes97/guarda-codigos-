
# Definindo funções
''' Funções são pequenos trechos de códigos que realizar tarefas específicas;
 Pode ou não receber entradas de dados e retornar uma saída de dados;
 Muito uteis para executar procedimentos similares por repetidas vezes;

 OBS: Se você escrever uma função que realiza várias tarefas dentro dela;
 é bom fazer uma verificação para que a função seja simplificada.

já utilizamos várias funções desde que iniciamos este curso:
-print()
-len()
-max()
-min()
-count()
- e muitas outras ;

# Exemplo de utilização de funções
cores = ['verde', 'amarelo', 'azul', 'branco']
# Utilizando a função integrada (Built-in) do Python print()
print(cores)
cores.append('roxo')
print(cores)
'''
# lllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllll
# Funções com retorno
'''
numeros = [1, 2, 3]
ret_pop = numeros.pop()
print(f'Retorno de pop: {ret_pop}')
ret_pr = print(numeros)
print(f'Retorno de print:{ret_pr}')

OBS: Em Python quando uma função retorna nenhum valor, o retorno é None
OBS: Funções python que retornam valores, devem retornar estes valores com a 
palavra reservada return.
OBS: Não precisamos necessariamente criar uma variavel para receber o retorno da uma função. 
Podemos passar a execução da função para outras funções 

# Exemplo função
# def quadrado_de_7():
#     print(7*7)
#
# ret = quadrado_de_7()
# print(f'Retorno{ret}')

# Vamos refaturar esta função para que ela retorne o valor

def quadrado_de_7():
    return 7*7
# Criamos uma variável para receber o retorno da função
ret = quadrado_de_7()
print(f'Retorno{ret}')
print(f'Retorno:{quadrado_de_7()+1}')'''
# Funções com parametros (de entrada)
'''-Funções que recebem dados para serem processados dentro da mesma;
Se a gente pensar em um programa qualquer, geralmente temos;
entrada -> processamento -> saída
Se a gente pensar em função, já sabemos que temos funções que :
    Não possuem entrada;
    Não possuem saída
    Possuem entrada mas não possuem saída;
    Não possuem entrada mas possuem saída;
    Possuem entrada e saída

# Nomeando parâmentros 
def nome_completo(nome, sobrenome):
    return f'Seu nome completo é {nome} {sobrenome}'
print(nome_completo('Angelina', 'Jolie'))'''
# A diferença entre Parâmetros e Argumentos
# Parâmetros são variaveis declaradas na definição de uma função;
# Argumentos são dados passados durante a execução de uma função;
# A ordem dos parâmetros importa !!
