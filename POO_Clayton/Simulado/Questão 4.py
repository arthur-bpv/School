''' 4) Escreva um algoritmo que receba uma lista de números e retorne a soma cumulativa; isto é, uma nova lista onde o i-ésimo elemento
é a soma dos primeiros i+1 elementos da lista original.
Exemplo: entrada: [1,2,3,4]     [1,3,4,5]
                Saida: [1,3,6,10]       [1,4,8,13]'''

entrada = [int(i) for i in input().split()]
soma_cumulativa = [sum(entrada[:i+1]) for i in range(len(entrada))]
print("Soma cumulativa:", soma_cumulativa)
