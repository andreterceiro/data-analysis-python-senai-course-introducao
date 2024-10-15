# Introdução

Eu colocarei anotações aqui de alguns tópicos que eu não achar tão óbvios do curso.


## Precedência:

```
P => ()
E => **
M => *
D => /
A => +
S => -
```

![precedencia](images/precedencia.png)

## Métodos de listas

Devo estar atento que posso fazer determinadas coisas em listas por métodos, como

```
a = [0,1,2]
a.append(3)
print(a) # [0,1,2,3]
```

E outras por palavras chave da linguagem:
```
del a[1]
print(a) # [0,2,3]
```

del a[1] pode ser chamado como função (= del(a[1]))

O método insert também insere, mas precisa da posição (PRECISA ser passado este argumento):
list.insert(location, value)

```
a = [1,3]
a.insert(1, 2)
print(a) # [1,2,3]
```

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

![operador inversao valores de variaveis](images/operador-inversao-valores-variaveis.png)

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


## Ordenação pelo método bolha

O curso fala de ordenação pelo método bolha. Como eu lembro isto do curso técnico (que ocorreu há mais de 20 anos kkk), eu fiquei com vontade de implementar. Eu implementei [aqui](https://github.com/andreterceiro/bubble-sort-python).


## Listas copiadas por referência

As listas são copiadas por referência. O trecho abaixo retorna `[2]`

```
list_1 = [1]
list_2 = list_1
list_1 [0] = 2
print(list_2)
```

Mas podemos fazer uma copia dos valores e gerar uma nova lista, como no *snippet* abaixo:

```
list_1 = [1]
list_2 = list_1[:]
list_1[0] = 2
print(list_2)
```

Isto é chamado de **fatiamento** ou **slicing**.

Desta forma podemos copiar apenas parte de uma lista, como no *snippet* abaixo:

```
# Copiando parte da lista.
my_list = [10, 8, 6, 4, 2]
new_list = my_list [1 : 3]
print(new_list) # [8, 6]
```

O formato é `[start: end]`, mas **end** é o primeiro elemento **não** incluso, como você pode deduzir do código acima.

No fatiamento podemos até trabalhar com números negativos. Números negativos fazem a contagem de elementos da lista de trás para frente. **-1** refere-se ao último elemento, mas lembre-se, **o último elemento não é incluído no retorno.**

Exemplos:

```
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:-1]
print(new_list) # [8, 6, 4]

my_list = [10, 8, 6, 4, 2]
new_list = my_list[-3:-1]
print(new_list) # [6, 4]
```

Mas como então falo que quero o **último** elemento de uma lista?

Bem, o último elemento no fatiamento pode ser omitido:

```
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:]
print(new_list) # [8, 6, 4, 2]
```

Podemos omitir também o índice de início do fatiamento. Veja:

```
my_list = [10, 8, 6, 4, 2]
new_list = my_list[:2]
print(new_list) # [10, 8]
```

Veja que da mesma forma que quando queremos retornar o último elemento e ocultamos o final no fatiamento (veja 2 exemplos de código acima), se ocultarmos o início do fatiamento, ele começa a retornar a partir do primeiro elemento.

**del** também pode ser feito em fatias. Lembre-se que o **índice final de fatiamento não é correspondente ao último índice excluído, e sim ele -1**. Veja:

```
my_list = [10, 8, 6, 4, 2]
del my_list[1:3]
print(my_list) # retorna [10, 4, 2]
```

Uma nova lista **não** é gerada!

Como esperado, `[:]` exclui todos elementos da lista:

```
lst = [1,2,3]
del lst [:] # list agora será igual a []
print(lst) # retorna []
del lst # assim eu excluo a lista e não seus elementos
print(lst) # Erro!
```


## in e not in em listas

```
my_list = [0, 3, 12, 8, 2]

print(5 in my_list)
print(5 not in my_list)
print(12 in my_list)

# Retorna
# False
# True
# True
```


# Falando um pouco sobre o "for"

O básico de uma iteração com **"for"** é:

```
lista = [4,5,6]
for elemento in lista:
    print(elemento)
```

Imprime:

4
5
6

Com **enumerate(lista)** conseguimos ter acesso ao **índice** em um loop semelhante, veja:

```
lista = [4,5,6]
for idx, elemento in enumerate(lista):
    print(str(idx) + ": " + str(elemento))
```

Imprime:

0: 4
1: 5
2: 6

Curiosidade, veja o *snippet* abaixo:

```
lista = [4,5,6]
print(enumerate(lista))
```

Retorna por exemplo:

<enumerate object at 0x7f41f1211500>

**Atenção:** não se pode fazer:

```
lista = [4,5,6]
print(enumerate(lista))
print(enumerate[0]) # Erro!!!!!!!!!!!!!
```

Lembre-se que a função, por exemplo com os parâmetros start e stop, retorna:

```
lista = range(4, 7)
print(lista) # retorna range(4, 7)
print(lista[0]) # retorna 4 - primeiro elemento
print(lista[-1]) # retorna 6 - último elemento
```

De vez em quando vemos um `for` com um `range`. Funciona como o esperado:

```
lista = range(4, 7)
for elemento in lista:
    print(elemento)

# Imprime
# 4
# 5
# 6
```


## Mais sobre fatiamento

Lembre-se que no fatiamento trabalhamos com os **índices**, logo `lst[1]` refere-se ao segundo elemento de uma lista. Para mostrar todos elementos da lista devemos começar no 0.

```
my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
 
for i in my_list[0:]:
    print(i)
```

Imprime:
17
3
11
5
1
9
7
15
13


# del em listas apontando para o mesmo lugar

Veja que quando excluímos uma lista, na verdade estamos excluindo o apontamento para ela. Ou seja, se existirem demais apontamentos para a lista, eles poderão continuar vendo a lista **mesmo que o primeiro apotamento seja removido**:

```
list_1 = ["A", "B", "C"]
list_2 = list_1
list_3 = list_2
 
del list_2[0]
del list_1
 
print(list_3) # Imprime [B, C]
```


# Compreensão de listas

```
row = ["banana" for i in range(8)]
print(row)

# Imprime:
['banana', 'banana', 'banana', 'banana', 'banana', 'banana', 'banana', 'banana']

# Lembre-se, range(8) retorna um range, mas semelhante a um array indo de 0 a 7
```


## Arrays multidimensionais com for ... in ...

Python tem uma sintaxe estranha para criar um array multidimensional com `for ... in ...`:

```
row = [["banana" for i in range(8)] for j in range(6)]
   
print(row)

# Imprime:
# [
#     ['banana', 'banana', 'banana', 'banana', 'banana', 'banana', 'banana', 'banana'], 
#     ['banana', 'banana', 'banana', 'banana', 'banana', 'banana', 'banana', 'banana'], 
#     ['banana', 'banana', 'banana', 'banana', 'banana', 'banana', 'banana', 'banana'], 
#     ['banana', 'banana', 'banana', 'banana', 'banana', 'banana', 'banana', 'banana'], 
#     ['banana', 'banana', 'banana', 'banana', 'banana', 'banana', 'banana', 'banana'], 
#     ['banana', 'banana', 'banana', 'banana', 'banana', 'banana', 'banana', 'banana'], 
# ]
```

Imprime em uma única linha, só formatei assim para facilitar a visualização. Veja, acima temos 8 elementos dentro de cada linha e 6 linhas, não confundir.


## For ... else

Como último "suspiro" de uma iteração, podemos colocar nela um bloco "`else`":

```
for element in range(0,3):
    print(element)
else:
    print("final")
```

Imprime:
0
1
2
final


## Funções


### Parâmetros


#### Geral

Quanto aos parâmetros, sem "novidades":

- Pode existir um valor padrão;
- Argumentos sem valor padrão devem vir no final;

```
def message(text2, text1="123"):
    print(text1, text2)

message("456")

# Imprime:
# 123 456
```


#### Passando o nome de um parâmetro


```
def introduction(first_name, last_name):
    print("Olá meu nome é", first_name, last_name)
 
introduction(first_name = "James", last_name = "Bond")
introduction(last_name = "Skywalker", first_name = "Luke")
```

Isto imprime:

```
Olá meu nome é James Bond
Olá meu nome é Luke Skywalker
```


#### Misturando keyword com positional arguments:

Podemos fazer testes estranhos (kkk):

```
def adding(a, b, c):
    print(a, "+", b, "+", c, "=", a + b + c)

adding(1, 2, 3) # Obviamente funciona, imprime '1+2+3=6'
adding(1, c=2, b=3) # Obviamente funciona, imprime '1+3+2=6'
adding(1, b=2) # Não funciona, pois falta o parâmetro 'c'
adding(a=2, b=3, 1) # Não funciona, pois o positional argument deve vir primeiro que o keyword argument
adding(2, 3, a=1) # Não funciona, pois temos múltiplos valores para 'a'
adding(2, 3, a=1, c=4) # Não funciona, pois temos múltiplos valores para 'a'
adding(2, 3, 4, d=5) # Não funciona, pois só temos 3 parâmetros
adding(1, 2, 3, 4) # Não funciona, pois só temos 3 parâmetros
```

** Um detalhe é que o `positional argument` deve vir antes do `keyword argument` 

Na declaração de funções, os argumentos com um valor padrão devem vir depois dos arqumentos sem um valor padrão.

```
# Não funciona, um argumento com valor padrão está vindo antes de um argumento sem um valor padrão
def soma(a=1, b):
    return a + b

# Pode não ter nada errado na declaração da função HIPOTETICAMENTE, mas chamá-la assim não funciona
adding(a=2, b=3, 1) # Não funciona, pois o positional argument deve vir primeiro que o keyword argument
```


## Curiosidades sobre o None

None não pode ser somado a nada, nem a None mesmo.

Se uma função explicitamente não retornar nada, ela retornará None por padrão.


## Escopo

Veja que código interessante:

```
def my_function():
    print("Eu conheço aquela variável?", var)

var = 1
my_function()
print(var)
```

É impresso "Eu conheço aquela variável?, 1". Ou seja, eu consigo acessar váriáveis externas a uma função dentro de uma função. Vou testar o inverso:

```
def my_function():
    var = 1
    print("Oi")

my_function()
print(var)
```

Erro, ou seja, o inverso não é verdadeiro, no escopo global eu não posso acessar uma variável declarada dentro de uma função.

Vamos testar se conseguimos alterar uma variável do escopo global por dentro de uma função:


```
def my_function():
    var = 2
    print("Oi", var)

var = 1
my_function()
print(var)
```

Não, o valor não é alterado no escopo global... Mas no escopo da função é sim, tanto que a linha

```
print("Oi", var)
```

Imprimiu "Oi 2", mas o `print(var)` do final, após a alteração dentro do escopo da função, imprimiu 1.

E se eu imprimir o valor antes da variável ser alterada, algo como:

```
def my_function():
    print("Oi", var)
    var = 2
    print("Oi", var)

var = 1
my_function()
print(var)
```

Isto gerará um erro de que a variável foi usada antes de ser declarada.


## Palavra chave 'global'

Vamos modificar um pouco o *snippet* anterior:

```
def my_function():
    global var
    print("Oi", var)
    var = 2
    print("Oi", var)

var = 1
my_function()
print(var)
```

Nenhum erro ocorre e eu consegui alterar a variável global. A saída é:

```
Oi 1
Oi 2
2
```


## Posso alterar uma variável passada como argumento?

Veja o código abaixo:

```
def my_function(n):
    print("Eu obtive", n)
    n += 1
    print("Eu tenho", n)

var = 1
my_function(var)
print(var)
```

A saída é:

```
Eu obtive 1
Eu tenho 2
1
```

Era o comportamento que se esperava, mas é importante reforçar kkk.

Mas veja que não é tão simples:

```
def my_function(my_list_1):
    print("Print #1:", my_list_1)
    print("Print #2:", my_list_2)
    del my_list_1[0] # Pay attention to this line.
    print("Print #3:", my_list_1)
    print("Print #4:", my_list_2)

my_list_2 = [2, 3]
my_function(my_list_2)
print("Print #5:", my_list_2)
```

A saída é:

```
Print #1: [2, 3]
Print #2: [2, 3]
Print #3: [3]
Print #4: [3]
Print #5: [3]
```

Neste caso eu alterei sim a variável passada como parâmetro.

E se eu adcionar um valor à lista?

```
def my_function(my_list_1):
    print("Print #1:", my_list_1)
    print("Print #2:", my_list_2)
    my_list_2.append(3)
    print("Print #3:", my_list_1)
    print("Print #4:", my_list_2)

my_list_2 = [2, 3]
my_function(my_list_2)
print("Print #5:", my_list_2)
```

Mesma coisa, alterei uma variável do escopo global, veja:

```
Print #1: [2, 3]
Print #2: [2, 3]
Print #3: [2, 3, 3]
Print #4: [2, 3, 3]
Print #5: [2, 3, 3]
```

E em relação a alterar 1 item?

```
def my_function(my_list_1):
    print("Print #1:", my_list_1)
    print("Print #2:", my_list_2)
    my_list_1[0] = 99
    print("Print #3:", my_list_1)
    print("Print #4:", my_list_2)

my_list_2 = [2, 3]
my_function(my_list_2)
print("Print #5:", my_list_2)
```

Mesma coisa, consegui alterar o conteúdo de uma variável que está no escopo global, veja a saída:

```
Print #1: [2, 3]
Print #2: [2, 3]
Print #3: [99, 3]
Print #4: [99, 3]
Print #5: [99, 3]
```

Vamos fazer um teste com uma lista que não seja passada como parâmetro:

```
def my_function():
    print("Print #1:", my_list_2)
    my_list_2[0] = 98
    my_list_2.append(99)
    del my_list_2[1]
    print("Print #2:", my_list_2)

my_list_2 = [2, 3]
my_function()
print("Print #3:", my_list_2)
```

Saída:

```
Print #1: [2, 3]
Print #2: [98, 99]
Print #3: [98, 99]
```

Ou seja, eu altero uma lista, que não é um escalar, do escopo global, passada como parâmetro ou não, se eu excluir, adicionar ou alterar um item da lista, mas se eu modificar a lista como um todo, simplesmente é mudado o apontamento. É o mesmo comportamento de eu ter 2 listas no escopo global e alterar uma, veja:

```
my_list_1 = [0,1,2]
my_list_2 = my_list_1
my_list_2[0] = 99
print(my_list_1)
print(my_list_2)
my_list_2 = "banana"
print(my_list_1)
print(my_list_2)
```

Saída:

```
[99, 1, 2]
[99, 1, 2]
[99, 1, 2]
banana
```

Ou seja, se eu alterar 1 item, altero de todas as varíaveis que tem o apontamento para a mesma lista, mas se eu alterar o **conteúdo todo** da variável, o apontamento novo muda, mas o antigo continua apontando para a mesma lista.


## Diversos

Criei a função abaixo para calcular um fatorial (em menos de 3 minutos kkk):

```
def factorial(number):
    total = 1
    while number > 1:
        total *= number
        number = number - 1

    return total
```

Testei com números aleatórios e deu certo :)
