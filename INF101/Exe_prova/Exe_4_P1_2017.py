def calcular_media(lista_de_tuplas):
    """
    Calcula a média das notas em uma lista de tuplas (matrícula, nota).

    Args:
    lista_de_tuplas (list): Uma lista de tuplas no formato (matrícula, nota).

    Returns:
    float: A média das notas.
    """
    if not lista_de_tuplas:
        return 0.0

    soma_das_notas = sum(nota for matricula, nota in lista_de_tuplas)
    numero_de_alunos = len(lista_de_tuplas)

    media = soma_das_notas / numero_de_alunos

    return media


# Exemplo de uso da função
notas = [(1, 85), (2, 90), (3, 78), (4, 92), (5, 88)]

media = calcular_media(notas)

print(f"A média das notas é: {media:.2f}")
