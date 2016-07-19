x = int(input("digite a data:"))
y = int(input("digite a hora:"))
m = int(input("digite os minutos:"))
z = int(input("digite os segundos:"))

x = x *24 *3600
y = y *3600
m = m *60
total = x+y+m+z
print(total,"segundos")