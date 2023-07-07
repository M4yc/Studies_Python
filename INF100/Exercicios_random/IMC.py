#Calculo de IMC
#imc=massa/altura*2
massa = float(input('Informe seu peso:'))
alt = float(input('Informe sua altura:'))
imc=massa/(alt**2)
print('Este é o seu undice de imc: %.2f' % imc)
if imc > 30:
    print('Obeso')
elif imc > 25:
    print('Sobrepeso')
elif imc > 18:
    print('Peso ideal')
elif imc < 18:
    print('Abaixo do peso')