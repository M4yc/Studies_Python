def calc(matr):
    matricula = [3,4,5,2,1]
    peso = [5,7,5,7,5]
    soma = 0
    for i in range(0,len(matricula)):
        soma = soma + int(matr[i]*peso[i])
    resto = soma % 11
    if resto < 2:
        dig = str(0)
    else:
        dig = str(11 - resto)
    return dig
def matrval(matr):
    return matr[5] == calc(matr)
