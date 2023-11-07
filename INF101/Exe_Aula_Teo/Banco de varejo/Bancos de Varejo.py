from bancos import Cliente, Conta

cliente1 = Cliente("João Silva", "3345-7890")
cliente2 = Cliente("Maria Silva", "3345-7890")
conta1 = Conta([cliente1], '0001', 1000.00)
conta2 = Conta([cliente1, cliente2], '0002', 500.00)
conta1.saque(50.00)
conta2.deposito(300.00)
conta1.saque(190.00)
conta2.deposito(95.26)
conta2.saque(245.00)
conta1.extrato()
conta2.extrato()