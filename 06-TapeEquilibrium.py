
'''Uma matriz não vazia A que consiste em N números inteiros é fornecida. A matriz A representa números em uma fita.

Qualquer número inteiro P, tal que 0 <P <N, divide esta fita em duas partes não vazias:
A [0], A [1], ..., A [P - 1] e A [P], A [ P + 1], ..., A [N - 1].

A diferença entre as duas partes é o valor de:
 | (A [0] + A [1] + ... + A [P - 1]) - (A [P] + A [P + 1] + .. . + A [N - 1]) |

Em outras palavras, é a diferença absoluta entre a soma da primeira parte e a soma da segunda parte.

Por exemplo, considere a matriz A de modo que:

  A [0] = 3
  A [1] = 1
  A [2] = 2
  A [3] = 4
  A [4] = 3
Podemos dividir esta fita em quatro lugares:

P = 1, diferença = | 3 - 10 | = 7
P = 2, diferença = | 4 - 9 | = 5
P = 3, diferença = | 6 - 7 | = 1
P = 4, diferença = | 10 - 3 | = 7
Escreva uma função:

solução def (A)

que, dada uma matriz não vazia A de N números inteiros, retorna a diferença mínima que pode ser alcançada.

Por exemplo, dado:

  A [0] = 3
  A [1] = 1
  A [2] = 2
  A [3] = 4
  A [4] = 3
a função deve retornar 1, conforme explicado acima.

Escreva um algoritmo eficiente para as seguintes suposições:

N é um número inteiro dentro do intervalo [2..100.000];
cada elemento da matriz A é um número inteiro dentro do intervalo [-1.000..1.000].'''

#A = [3, 1, 2, 4, 3]
#def solution(A:list):
   # cont = 1
   # diferenca = 0
   # dif = sum(A)
   # for i in range(0,len(A)):
   #     lista1 = []
     #   lista1 = A.split(5)
      #  #lista1 = A.split(A[cont])
     #   lista1 = sum(lista1)
    #    if lista1 < dif:
   #         diferenca == (sum(lista1))
  #      cont +=1
 #   return diferenca

#print(solution(A))

#lista1 = []
#lista1 = A.split


A = [3, 1, 2, 4, 3,0,5,8,9]
def solution(A:list):
    diferenca_total = abs(sum(A))
    for i in range(0,len(A)):
        somaA = sum(A[0:i+1])
        somaB = sum(A[i+1:])
        diferenca = abs(somaA - somaB)
        if diferenca < diferenca_total:
            diferenca_total = diferenca
    return diferenca_total

print(solution(A))