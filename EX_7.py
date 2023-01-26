import random

v = [0] * 5

def vetor():
  for i in range(len(v)):
    v[i] = random.randint(1,10)
vetor()
print(v)


x = int(input('insira um número natural: '))

cont = 0
j = 0
if x in v: 
    while x != v[j]:
        cont += 1
        j += 1
    print(cont)
else:
    print(-1)
