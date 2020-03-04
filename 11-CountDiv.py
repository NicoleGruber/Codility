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
A = 101
B = 123000000
K = 10000
def solution (A, B, K):
    lista_num = []
    div = []
    for i in range(A,B+1):
        #if i % K== 0:
            #lista_num.append(i)
        div = set(i % K == 0)
    return len(div)



print(solution(A,B,K))