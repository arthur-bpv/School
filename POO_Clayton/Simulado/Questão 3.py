'''3) Escreva um algoritmo que receba uma lista do usuário e informe se a lista tem números repetidos ou não. Se sim, informe quais são os números repetidos.
Exemplo: entrada: 1 1 2 3
               saida: o número 1 se repete 2 vezes
               entrada: 2 2 3 4 3
               saida: o número 2 se repete 2 vezes
                        o número 3 se repete 2 vezes'''

entrada = [int(i) for i in input().split()]
for num in set(entrada):
    if entrada.count(num) > 1:
        print(f"O número {num} se repete {entrada.count(num)} vezes")
