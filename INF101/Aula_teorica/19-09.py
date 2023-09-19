arq = open("resultados.txt","w")
for linha in range(1,101):
    arq.write("%d\n" % linha)

arq.close()