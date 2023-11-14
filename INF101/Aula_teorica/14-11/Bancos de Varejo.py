from bancos import Cliente, Conta, Banco
from heranca import ContaEspecial

cliente1 = Cliente("João Silva", "3456-7890")
cliente2 = Cliente("Maria Silva", "3456-7890")
cliente3 = Cliente("José Vargas", "2351-1809")

contaJM = Conta([cliente1, cliente2], '76534', 100.00)
contaJ= Conta([cliente3], '80297', 10.00)

banco1 = Banco("Tatu")
banco1.abreConta(contaJM)
banco1.abreConta(contaJ)
banco1.listaContas()

# print( type(banco1.contas[0].clientes[0].nome) )
print( banco1.contas[0].clientes[0].nome )
print( banco1.contas[0].clientes[1].nome )
# print( banco1.contas[0].clientes[2].nome )
print( banco1.contas[1].clientes[0].nome )

contaJJ = Conta([cliente1,cliente3], '00001', 500)

banco1.abreConta(contaJJ)
banco1.listaContas()