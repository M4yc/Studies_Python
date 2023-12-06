# banco.py
# Luiz C. A. Albuquerque
# lcaa@ufv.br
# 14/11/2023
# Define classes para modelar um banco de varejo.

class Cliente:

    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

        
class Conta:

    def __init__(self, clientes, numero, saldo=0.00):
        self.clientes = clientes
        self.numero = numero
        self.saldo = 0.00
        self.operacoes = []
        self.deposito(saldo)  # primeira operação na conta

    def resumo(self):
        print("CC nº %s Saldo: %10.2f" % (self.numero, self.saldo))

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.operacoes.append(("SAQUE", valor))
        else:
            print("\n***CC nº %s: saque de %.2f não realizado; "
                  "saldo disponível de %.2f\n" % (self.numero, valor,
                  self.saldo))

    def deposito(self, valor):
        self.saldo += valor
        self.operacoes.append(("DEPÓSITO", valor))

    def extrato(self):
        print("\n\nExtrato CC nº %s\n" % self.numero)
        for op in self.operacoes:
            print("%10s %10.2f" % op)
        print("\n     SALDO %10.2f" % self.saldo)

class Banco:
    
    def __init__(self, nome):
        self.nome = nome
        self.contas = []
        
    def abreConta(self, conta):
        self.contas.append(conta)
        
    def listaContas(self):
        print("\n\nContas do Banco %s\n" % self.nome)
        for c in self.contas:
            c.resumo()
            
        
# Teste das classes.
def main():
    cliente1 = Cliente("João Silva", "3234-7890")
    cliente2 = Cliente("Maria Silva", "3234-7890")
    cliente3 = Cliente("José Vargas", "2567-0987")
    cliente4 = Cliente("Marina Lima", "(21) 3509-4390")

    conta1 = Conta([cliente1, cliente2], "1", 1000.00)
    conta2 = Conta([cliente3], "2", 500.00)
    conta3 = Conta([cliente4], "3")
    
    banco = Banco("Tatu")
    banco.abreConta(conta1)
    banco.abreConta(conta2)
    banco.abreConta(conta3)

    conta1.saque(50.00)
    conta2.deposito(300.00)
    conta1.saque(190.00)
    conta2.deposito(95.15)
    conta2.saque(256.71)
    conta3.saque(102.85)    # este saque não será realizado; conta sem saldo
                            # suficiente

    conta1.resumo()
    conta2.resumo()

    conta1.extrato()
    conta2.extrato()
    conta3.extrato()
    
    banco.listaContas()


if __name__ == "__main__":
    main()
