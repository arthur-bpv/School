# exemplo de classe

class Conta:
    agencia = ""
    numero = ""
    saldo = 0.0

    # Método depositar
    def deposita(self, valor):
        self.saldo += valor

    # Método sacar
    def saca(self, valor):
        self.saldo -= valor

Conta1 = Conta()
Conta1.agencia = '1234-5'
Conta1.numero = 1111-0
Conta1.saldo = 100

print(Conta1.agencia)
print(Conta1.saldo)
print(Conta1.numero)

Conta2 = Conta()
Conta2.agencia = '1111-2'
Conta2.numero = '2222-0'
Conta2.saldo = 300

print(Conta2.agencia)
print(Conta2.numero)
print(Conta2.saldo)
