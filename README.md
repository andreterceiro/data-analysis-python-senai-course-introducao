# Introduction

Eu colocarei anotações aqui de alguns tópicos que eu não achar tão óbvios do curso.


## Precedência:

P => ()
E => **
M => *
D => /
A => +
S => -

![precedencia](images/precedencia.png)

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