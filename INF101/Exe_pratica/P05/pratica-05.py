#Nome: Maycon Vinicius Batista Araújo
#matricula: 113683
#Data: 21/09/2023
#Programa para verificar uma estrutura de pilha


def analise_parenteses(expressao):
    pilha=[]
    for c in expressao:
        if c == "(":
            pilha.append("(")
        elif c == ")":
            if len(pilha) == 0:
                return False
            else:
                pilha.pop()
    if len(pilha) == 0:
        return True
    else:
        return False
    
def main():

    expre = input("Digite uma expressão com parênteses (ENTER para terminar): ")
    while True:
        if expre == "":
            break
        if analise_parenteses(expre) == True:
            print("%s está OK" % expre)
        if analise_parenteses(expre) == False:
            print("%s está ERRADO" % expre)
        expre = input("Digite uma expressão com parênteses (ENTER para terminar): ")
        
main()
    

