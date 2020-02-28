def solution(N):
    num_bin = bin(N)[2:]
    resultado = num_bin.strip('0').strip('1').split('1')
    resultado = len(max(resultado))
    return resultado