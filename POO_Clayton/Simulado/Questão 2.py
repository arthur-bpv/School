'''2)Escreva um algorítmo que receba uma lista do usuário e informe ao usuário se a lista está ordenada em ordem cresente ou decrescente ou está desordenada.
Exemplo: entrada: 1 3 3 5 7
               saida: cresente
               entrada: 4 3 2 2 2
               saida: decrescente'''


entrada = [int(i) for i in input().split()]

if entrada == sorted(entrada):
    print("A lista está: crescente")
elif entrada == sorted(entrada, reverse=True):
    print("A lista está: decrescente")
else:
    print("A lista está: desordenada")




