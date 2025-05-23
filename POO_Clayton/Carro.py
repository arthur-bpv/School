class Carro:
    marca = ""
    modelo = ""
    ano = 2000
    preco = 0.0

    # Método aumentar 10%

    def aumenta10(self):
        self.preco *= 1.1

    def diminuir10(self):
        self.preco *= 0.9

carro1 = Carro()
carro1.marca = input('Informe uma marca: ')
carro1.modelo = input('Informe uma modelo: ')
carro1.ano = int(input('Informe uma ano: '))
carro1.preco = float(input('Informe uma preco: '))

# print(f"Marca: {carro1.marca}")
# print(f"Modelo: {carro1.modelo}")
# print(f"Ano: {carro1.ano}")
# print(f"Preço: {carro1.preco}")

print('Aumentando preço:')

carro1.aumenta10()

print(f"Preço: {carro1.preco:.2f}")

print('Diminuindo preço:')

carro1.diminuir10()

print(f'preço: {carro1.preco:.2f}')