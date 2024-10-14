# Introduction

Eu colocarei anotações aqui de alguns tópicos que eu não achar tão óbvios do curso.


## Precedência:

P => ()
E => **
M => *
D => /
A => +
S => -


## Métodos de listas

Devo estar atento que posso fazer determinadas coisas em listas por métodos, como
a = [0,1,2]
a.append(3)
print(a) # [0,1,2,3]

E outras por palavras chave da linguagem:
del a[1]
print(a) # [0,2,3]

del a[1] pode ser chamado como função (= del(a[1]))

O método insert também insere, mas precisa da posição (PRECISA ser passado este argumento):
list.insert(location, value)

a = [1,3]
a.insert(1, 2)
print(a) # [1,2,3]

Atenção! O insert EMPURRA os demais valores, não sobrescreve. Reforçando:

```
my_list = []  # Criando uma lista vazia.
 
for i in range(5):
    my_list.insert(0, i + 1)
 
print(my_list) # [5,4,3,2,1]
```

Sobre a função range(), memorize que o comportamento dela difere dependendo do número de argumentos:

range(number) # cria uma lista de 0 até o número passado
range(start, stop) # cria uma lista de start a stop (veja o exemplo abaixo). stop NÃO deve ser incluído (só é incluído 1 inteiro antes)
range(start, stop, step) # cria uma lista de start a stop, pulando de step em step. stop NÃO deve ser incluído (só é incluído 1 inteiro antes)

```
>>> print(range(100)[99]) # lista com números de 0 a 99
99
>>> print(range(100, 101)[0]) # [100]
100
>>> print(range(100, 105, 2)[2]) # [100, 102, 104]
104
```

É interessante que é possível executar o comando abaixo:
range(-2)

Um número negativo como parâmetro. Mas isto dá erro:
range(-2)[0]

OBS: range(2)[0] retorna 0.

E range(-1), com um número negativo como parâmetro, dá erro


## Troca de valores entre variáveis

É possível fazer isto para trocar o valor de duas variáveis:
variable_1, variable_2 = variable_2, variable_1

Este script inverte a lista, mas por causa do break:

a = [0, 1, 2, 3, 4, 5]

```
for i in a:
    print(i)
    a[i] , a[len(a) - i - 1] = a[len(a) - i - 1], a[i]
    if i == 2:
        break

print(a)
```

Se não tiver o break, ele inverte e “desinverte” depois.


## del

del pode ser usado em listas ou em escalares:

```
a = 1
del a
print(a) # Erro !!

a = [0,1,2]
del a[1]
print(a) # [0,2]
```





