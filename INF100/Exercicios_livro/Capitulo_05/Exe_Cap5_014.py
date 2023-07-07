#Salario Base
sala_base = float(input("Informe o salario base: "))
cod = int(input("Infome o Código de Funcionario: "))

if cod == 1:
    aumento = sala_base * 0.75
    sala_bruto = sala_base + aumento
    print("Diretor recebeu um aumento de 75%")
    print("Salario bruto = %.2f" % sala_bruto)
elif cod == 2:
    aumento = sala_base * 0.20
    sala_bruto = sala_base + aumento
    print("Secretário recebeu um aumento de 20%")
    print("Salario bruto = %.2f" % sala_bruto)
elif cod == 3:
    aumento = sala_base * 0.10
    sala_bruto = sala_base + aumento
    print("Atendente recebeu um aumento de 10%")
    print("Salario bruto = %.2f" % sala_bruto)
elif cod == 4:
    aumento = sala_base * 0.30
    sala_bruto = sala_base + aumento
    print("Caixa recebeu um aumento de 30%")
    print("Salario bruto = %.2f" % sala_bruto)
elif cod == 5:
    aumento = sala_base * 0.50
    sala_bruto = sala_base + aumento
    print("Gerente recebeu um aumento de 50%")
    print("Salario bruto = %.2f" % sala_bruto)