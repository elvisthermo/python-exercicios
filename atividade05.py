x = float(input("preço da mercadoria:"))
por = float(input('digite percentual de desconto:'))
rest = x*por/100
total = x-rest
print(total,'$ valor total',rest,'$ valor do desconto' )