#sequencia de fibonacci #

n = int(input('n:'))
a, b = 1, 1

f = 1
while f<= n-2 :
    a, b= b, a+b
    f = f+1
    print('fibonacci(%d)=%d' %(f,b))