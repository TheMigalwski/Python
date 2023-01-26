import random

1vetor = [0] * 3
2vetor = [0] * 3

for i in range(len(vet1)):
    1vetor[i] = random.randint(1,10)
    2vetor[i] = random.randint(1,10)

print('vet1 = {}{}, {}, {}{}'.format('{',1vetor[0], 1vetor[1], 1vetor[2],'}'))
print('vet2 = {}{}, {}, {}{}\n'.format('{',2vetor[0], 2vetor[1], 2vetor[2],'}'))

x = 1vetor[0] + 2vetor[0]
y = 1vetor[1] + 2vetor[1]
z = 1vetor[2] + 2vetor[2]
print('força resultante: ({}, {}, {})'.format(x, y, z))
