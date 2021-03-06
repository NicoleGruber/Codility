'''Uma matriz não vazia A que consiste em N números inteiros é fornecida. A matriz contém um número ímpar de elementos e cada elemento da matriz pode ser emparelhado com outro elemento que tem o mesmo valor, exceto por um elemento que não é emparelhado.

Por exemplo, na matriz A, de modo que:

  A [0] = 9 A [1] = 3 A [2] = 9
  A [3] = 3 A [4] = 9 A [5] = 7
  A [6] = 9
os elementos nos índices 0 e 2 têm valor 9,
os elementos nos índices 1 e 3 têm valor 3,
os elementos nos índices 4 e 6 têm valor 9,
o elemento no índice 5 tem valor 7 e não está emparelhado.
Escreva uma função:

solução def (A)

que, dada uma matriz A que consiste em N números inteiros que atendem às condições acima, retorna o valor do elemento não emparelhado.

Por exemplo, dada a matriz A de modo que:

  A [0] = 9 A [1] = 3 A [2] = 9
  A [3] = 3 A [4] = 9 A [5] = 7
  A [6] = 9
a função deve retornar 7, conforme explicado no exemplo acima.

Escreva um algoritmo eficiente para as seguintes suposições:

N é um número inteiro ímpar dentro do intervalo [1 .. 1.000.000];
cada elemento da matriz A é um número inteiro dentro do intervalo [1..1.000.000.000];
todos, exceto um dos valores em A, ocorrem um número par de vezes.'''

def solution(A):
    A.sort()                    #Colocando os numeros inteiros da lista em ordem crescente
    if len(A) == 1:             #Verificando se a lista contem apenas 1 elemento
        return A[0]                #Se tiver apenas 1, retornando esse numero
    for i in range(0,len(A),2): #FOR para ir verificando na lista de dois em dois elementos
        if i == len(A) - 1:     #Verificando se o numero mais alto que é o numero que não tem repeticao
            return A[i]            #Se for, retorna o numero
        if A[i] != A[i + 1]:    #Fazendo a verificão dos demais numeros
            return A[i]            #Retorna o numero sem repeticao
