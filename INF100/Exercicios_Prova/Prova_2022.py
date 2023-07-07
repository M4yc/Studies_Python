a = int(input("a = "))
b = -2
c = a+4%b
d= -b // 2 * a
print('A = %d, b = %d, c = %d, d = %d' %(a,b,c,d))
a = 2
print('c =',c)
if a>0:
    if a<6 and b!= -2:
        print('saída IF: ', a,b,c,d)
        a=b+1
        b=a-2
    elif a == 10 or b<a:
        print('saida ELIF: ', a,b,c,d)
        b=a+1
        a=b-1
    else:
        print('saída ELSE: ', a,b,c,d)
        b=a+2
        a=b+1
    c=a-2
else:
    print('saída a<=0', a,b,c,d)
    c = a+b
    d=d+3
d=5
print('FINAL: ',a,b,c,d)