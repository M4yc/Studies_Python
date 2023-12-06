# Nome do arquivo fonte: p02.py
# Nome do programador: Maycon Vinicius
# Matrícula: 113683
# Data: 24/08/2023
# Faz o calculo de media,desvio padrao, valor minimo e valor maximo das notas fornecidas
#

import math
import numpy as np

def main():
    nomeArq  = 'notas_inf100.dat'
    arqNotas = open(nomeArq, 'r')
    linhas = arqNotas.read().split('\n')
    arqNotas.close()

    notas = np.array(list(map(float, linhas)))

    print('%d notas lidas.' % len(linhas))
    print()
    print('Média das notas:         %5.1f' % media(notas))
    print('Desvio padrão das notas: %5.1f' % desvioPad(notas))
    print('Maior nota:              %5.1f' % maximo(notas))
    print('Menor nota:              %5.1f' % minimo(notas))

#
# Insira abaixo a implementação das funções requeridas:
#
def media(notas):
    soma = 0
    if len(notas) > 0:
        for i in range(0,len(notas)):
            soma += notas[i]
            
        media = soma/len(notas)
        return media
    else:
        return None
     
def desvioPad(notas):
    s=0
    
    if len(notas) > 1:
        for i in range(len(notas)):
            s+=(notas[i]-media(notas))**2
            desvio = math.sqrt(s/(len(notas)-1))
    

    else:
        return none
    
    return desvio
def maximo(notas):
    maximo = notas[0]
    for i in range (0,len(notas)):
        if notas[i] > maximo:
            maximo = notas[i]
    return maximo
        
def minimo(notas):
    minimo = notas[0]
    for i in range (0,len(notas)):
        if notas[i] < minimo :
            minimo = notas[i]
    return minimo

#
# Não mexa nestas linhas abaixo.
#
if __name__ == '__main__':
    main()

