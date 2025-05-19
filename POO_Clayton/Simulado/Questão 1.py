'''
1)Escreva um algoritmo que recebe uma lista do usuário e retorne uma nova lista com todos os elementos originais, exeto o primeiro e o último elemento da lista.
Exemplo: entrada: 1 2 3 4
               saida: 2 3'''

numeros =[int(i) for i in input().split()]
print(numeros[1:-1])


