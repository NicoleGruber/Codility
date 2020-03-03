'''Escreva uma função:

solução def (A, B, K)

que, dados três números inteiros A, B e K, retorna o número de números inteiros dentro do intervalo [A..B]
 que são divisíveis por K, ou seja:

{i: A ≤ i ≤ B, i mod K = 0}

Por exemplo, para A = 6, B = 11 e K = 2, sua função deve retornar 3, porque há três números divisíveis por
2 no intervalo [6..11], ou seja, 6, 8 e 10.

Escreva um algoritmo eficiente para as seguintes suposições:

A e B são números inteiros dentro do intervalo [0..2.000.000.000];
K é um número inteiro dentro do intervalo [1 .. 2.000.000.000];
A ≤ B.'''
A = 2
B = 10
K = 2
def solution (A, B, K):
    lista_num = []
    for i in range(A,B+1):
        resto = i % K
        if resto == 0:
            lista_num.append(i)
    return len(lista_num)



print(solution(A,B,K))