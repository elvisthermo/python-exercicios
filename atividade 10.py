dia = int(input('quantos cigarros por dia:'))
vid = int(input('quantos anos como fumante:'))
total_cigarros = vid*365*dia
perdidos = total_cigarros/144
print('perdeu aproximadamente %.2f dias'%perdidos)