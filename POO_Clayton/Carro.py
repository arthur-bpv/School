class Carro:
    marca = ""
    modelo = ""
    ano = 2000
    preco = 0.0

    # Método aumentar 10%

    def aumenta10(self):
        self.preco *= 1.1

carro1 = Carro()
carro1.marca = input('Informe uma marca: ')
carro1.modelo = input('Informe uma modelo: ')
carro1.ano = input('Informe uma ano: ')
carro1.preco = input('Informe uma preco: ')

print(f"Marca: {carro1.marca}")
print(f"Modelo: {carro1.modelo}")
print(f"Ano: {carro1.ano}")
print(f"Preço: {carro1.preco}")
