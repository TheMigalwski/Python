import random
vetor = [0] * 50 
for i in range(len(vetor)):
  vetor[i] = random.randint(1,6) 
print(vetor) 
cont = 0 
for j in range(len(vetor)):
  if vetor[j] == 6:
    cont = cont+1 
porcen = (cont/50)*100 
print("O percentual de ocorrência 6 é:" , porcen)
