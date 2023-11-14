from bancos import Conta, Cliente, Banco
class ContaEspecial(Conta):
    def __init__(self, clientes, numero, saldo=0, limite=0):
        super().__init__(clientes, numero, saldo)
        self.limite = limite

    def saque(self, valor):
        if (self.saldo + self.limite) >= valor:
            self.saldo -= valor
            self.operacoes.append(("SAQUE", valor))
