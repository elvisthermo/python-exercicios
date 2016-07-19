import random
li = []
while len(li) < 15:
    x = random.randint(10,100)
    if x not in li:
        li.append(x)
li.sort()
print(li)