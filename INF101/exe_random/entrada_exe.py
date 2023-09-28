# Código para criar o arquivo de entrada.

arq = open('entrada.txt','w')
conteudo = """
*Volta o cão arrependido
>Com suas orelhas tão fartas
<     Com seu osso roído
<E com o rabo entre as patas
;
;Volta o cão arrependido
Com suas orelhas tão fartas
>Com seu osso roído
E com o rabo entre as patas
"""
arq.write(conteudo)
arq.close()