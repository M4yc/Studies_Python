#Nome: Maycon Vinicius Batista Araujo
#Matricula: 113683
#Data: 14/09/2023
# Achar o segundo menor elemento de um conjunto de dados numéricos.

def main():
    l = [36, 18, 43, 9, 18, 25, 14]
    #l = [8, 7, 6, 5, 4, 3, 2, 2]
    #l = [36]
    print("Lista Original: ",l)
    #segundoMenor(l)
    print("Segundo Menor da lista: ",segundoMenor(l))

def segundoMenor(l):
    menor = l[0]
    if len(l) > 1:
        for i in range(len(l)):
            if l[i] < menor:
                menor = l[i]
            for j in range(len(l)):
                if l[j] > menor:
                    menor2 = l[j]
                elif l[j] == menor:
                    menor2 = l[j]
            
        return menor2
    
    else:
        return None
    
main()
