sal = int(input("digite o valor de seu salario:"))
por = int(input("digite o valor da porcetagem:"))
if sal and por > 0 :
    total = sal*por/100.0
    print(total)
else:
    print("o salario deve e a porcetagem devem ser positivos!")

