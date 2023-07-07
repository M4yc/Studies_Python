## Escreva um programa que verifique a validade de uma senha fornecida pelo usuário.
#A senha válida é 1234. Caso a senha informada pelo usuário seja inválida, a
#mensagem "ACESSO NEGADO" deve ser impressa e repetida a solicitação de uma
#nova senha até que ela seja válida. Caso contrário deve ser impressa a mensagem
#"ACESSO PERMITIDO" junto com um número que representa quantas vezes a
#senha foi informada.

senha_cor = "1234"
tent = 0

senha = str(input("Informe sua senha: "))

while senha != senha_cor:
    print("Acesso negado")
    senha = str(input("Informe sua senha: "))
    tent += 1
print("Acesso permitido, Numero de tentativas:%d " % (tent+1) )