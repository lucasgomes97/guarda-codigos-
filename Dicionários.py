# Dicionários
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

del receita['fev'] # Se achave não existir será gerado um keyError"""

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


#Métodos de dicionários .

d = dict(a=1, b=2, c=3)
print(d)
print(type(d))

#Limpar o dicionário (zerar dados)
d.clear()
print(d)

#Copiando um dicionario para outro 
#Forma1 Deep Copy
novo = d.copy()
print(novo)
novo['d']= 4 
print(d)
print(novo)
#Forma 2 Shallow Copy 
novo = d 
print(novo)
novo ['d']=4
print(d)
print(novo)

#Forma não usual de criação de dicionários 

outro = {}.fromkeys('a', 'b')

print(outro)
print(type(outro))

usuario= {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')
print(usuario)
print(type(usuario))

#OBS: o método fromKeys recebe dois parametros um interavel e um valor.
# ele vai gerar cada valor do interável uma chave e irá atribuir a esta chave o valor informado.

veja = {}.fromkeys('teste', 'valor')
print(veja)
veja1 = {}.fromkeys(range(1, 11),'novo')
print(veja1)'''
