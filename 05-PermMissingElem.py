'''É fornecida uma matriz A que consiste em N números inteiros diferentes. A matriz contém números inteiros no intervalo [1 .. (N + 1)], o que significa que exatamente um elemento está ausente.

Seu objetivo é encontrar esse elemento que está faltando.

Escreva uma função:

solução def (A)

que, dada uma matriz A, retorna o valor do elemento ausente.

Por exemplo, dada a matriz A de modo que:

  A [0] = 2
  A [1] = 3
  A [2] = 1
  A [3] = 5
a função deve retornar 4, pois é o elemento que falta.

Escreva um algoritmo eficiente para as seguintes suposições:

N é um número inteiro dentro do intervalo [0..100.000];
os elementos de A são todos distintos;
cada elemento da matriz A é um número inteiro dentro do intervalo [1 .. (N '''

A = [2]

def solution(A):
    A.sort()
    if len(A) == 0 or not 1 in A:
        return 1
    if len(A) == 1:
        return A[0]+1
    cont = 1
    for num in A:
        if num != cont:
            return cont
        cont += 1
    return cont


def SS(A):
    if len(A) == 1:
        return A[0] + 1
print(solution(A))

