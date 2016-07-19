a = int(input("digite o lado:"))
b = int(input("digite o lado:"))
c = int(input("digite o lado:"))

if a>b+c or b>a+c or c>a+b:
    print("não pode ser um tringulo")
    print("um dos lados e maior que a soma dos outos dois")
elif a== b ==c:
    print("equlilatero")
elif a==b or b==c or a==c:
    print("isocles")
else:
    print("escaleno")