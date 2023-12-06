#matricula: 113683
#nome: Maycon Vinicius Batista Araujo
#data: 16/11/2023
#Modelar um banco de varejo usando Classes

from banco import Cliente, Conta, Banco

class ContaEspecial(Conta):
        def __init__(self, clientes, numero, saldo=0.00, limite=0.00):
            super().__init__(clientes, numero, saldo)
            self.limite = limite

        def saque(self, valor):
            if (self.saldo + self.limite) >= valor:
                self.saldo -= valor
                self.operacoes.append(("SAQUE", valor))
                
            else:
                print("\n***CC nº %s: saque de %.2f não realizado; saldo disponível de %.2f" % (self.numero, valor, self.saldo + self.limite))

                
def main():
    
           
    cliente1 = Cliente("João Silva", "3456-7890")
    cliente2 = Cliente("Maria Silva", "3456-7890")
    cliente3 = Cliente("José Vargas", "2351-1809")
    cliente4 = Cliente("Marina Lima", "(21) 3509-4390")
    contaJM = ContaEspecial([cliente1, cliente2],"76534", 100.00, 500.00)
    contaJ = Conta([cliente3], "80297", 10.00)
    contaM = Conta([cliente4], "81020")
    banco = Banco("Tatu")
    
    banco.abreConta(contaJM)
    banco.abreConta(contaJ)
    banco.abreConta(contaM)
    banco.listaContas()
    
    contaJM.saque(50.00)
    contaJ.deposito(300.00)
    contaJM.saque(190.00)
    contaJ.deposito(95.26)
    contaJ.saque(245.00)
    contaJM.saque(654.38)# não será realizado; ultrapassa limite
    contaM.saque(102.85)# idem; conta sem saldo suficiente
    contaJM.extrato()
    contaJ.extrato()
    
    banco.listaContas()

if __name__ == "__main__":
    main()
