#exercicio da aula de Classes
class Cliente:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

class Conta:

  def __init__(self, clientes, numero, saldo=0) :
    self.clientes = clientes
    self.numero = numero
    self.saldo = 0.0
    self.operacoes = []
    if saldo > 0.0:
      self.deposito(saldo) # primeira operação

  def resumo(self):
    print("Cc nº {:s} Saldo: {:10.2f}".format(self.numero, self.saldo))

  def saque(self, valor):
    if self.saldo >= valor:
      self.saldo -= valor
      self.operacoes.append(("SAQUE", valor))
    else:
      print('Cc nº {} com saldo insuficiente; SAQUE NÃO REALIZADO'.\
            format(self.numero))

  def deposito(self, valor):
    self.saldo += valor
    self.operacoes.append(("DEPÓSITO", valor))

  def extrato(self):
    print("Extrato Cc nº {:s}\n".format(self.numero))
    for op in self.operacoes:
      print("{:10s} {:10.2f}".format(op[0], op[1]))

    print("\n Saldo: {:10.2f}\n".format(self.saldo))

class Banco:
  def __init__(self, nome):
    self.nome = nome
    self.contas = []

  def abreConta(self,conta):
    self.contas.append(conta)

  def listaContas(self):
    for c in self.contas:
      c.resumo()