from datetime import datetime

print('Este programa verifica se um número é primo')
print('Para encerrar o programa digite um número <= 0')

while True:
    num = int(input("Entre com um número N (>0): "))
    if num <= 0:
        break
    elif num % 2 == 0: #testa se é par
        print('%d não é primo' % num)
    else:
        start_time = datetime.now()
        divisor = 3
        limite = int(num**0.5)+1
        while divisor <= limite and num % divisor != 0:
            divisor = divisor + 2
        if divisor > num:
            print('%d é primo' % num)
        else:
            print('%d não é primo' % num)
        end_time = datetime.now()
        print("Início: %dh  %dm  %ds"%(start_time.hour, start_time.minute, start_time.second))
        print("Fim   : %dh  %dm  %ds" % (end_time.hour, end_time.minute, end_time.second))
        time_diff = (end_time - start_time)
        execution_time = time_diff.total_seconds() * 1000
        print("Tempo em milisegundos %.3f" %execution_time)
        print()