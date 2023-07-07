def calculaIMC(altura,peso):
    return peso/altura**2
def classificaIMC(imc):
    if imc < 18.6:
        return "Magreza"
    if imc >= 18.6 and imc < 24.9:
        return "Normal"
    if imc >= 25 and imc < 29.9:
        return "Sobrepeso"
    if imc > 29.9:
        return "Obesidade"

######## Programa Principal ############

peso = float(input('Informe seu peso (kg): '))
altura = float(input('Informe sua altura (m): '))
imc = calculaIMC(altura, peso)
cl = classificaIMC(imc)
print(f'IMC = {imc:.1f} é classificado como: {cl}')
