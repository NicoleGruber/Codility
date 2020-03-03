
'''Esta é uma tarefa de demonstração.

Escreva uma função:

def solution(A)

que, dada uma matriz A de N números inteiros, retorna o menor número inteiro positivo (maior que 0) que não ocorre em A.

Por exemplo, dado A = [1, 3, 6, 4, 1, 2], a função deve retornar 5.

Dado A = [1, 2, 3], a função deve retornar 4.

Dado A = [−1, −3], a função deve retornar 1.

Escreva um algoritmo eficiente para as seguintes suposições:

N é um número inteiro dentro do intervalo [1..100.000];
cada elemento da matriz A é um número inteiro dentro do intervalo [-1.000.000..1.000.000].'''


A = [-10,0, 2, 3,4,9,8,7,6,5,10,11,12,13,141]

def solution(A):
    a = set(A)
    cont = 0
    if not 0 in A:
        cont = 1
    for num in a:
        if num != cont:
            return cont
        if num == cont:
            cont += 1
    return cont

print(solution(A))










