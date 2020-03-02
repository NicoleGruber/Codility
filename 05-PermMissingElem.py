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
    A.sort()                        #Colocando a lista em ordem crescente
    if len(A) == 0 or not 1 in A:   #Verificando se os itens da lista  são == 0 ou se não tem o 1 na lista
        return 1
    if len(A) == 1:                 #Verificando se os itens da lista são == 1
        return A[0]+1
    cont = 1                        #Contador para verificação dos numeros inteiros da lista
    for num in A:                   #For para passar por todos os itens da lista
        if num != cont:             #Verificando se o numero é diferente do contador
            return cont             #Se for, ele retorna esse numero do contado que não tem na lista
        cont += 1
    return cont                     #Se o numero que tiver faltando for o depois, não o que esta no meio, ele retorna esse numero
