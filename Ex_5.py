import random

def Vetor(vetor):
    for i in range(len(vetor)):
        vetor[i]=random.randint(1,100)
    return vetor

def uni(A, B):
  ab1 = A + B
  ab2 = []
  ab3 = " "

  for i in ab1: 
    if i not in ab2:
      ab3 += str(i) + " "
      ab2.append(i) 
  return ab3

def main():
  A = [0]5
  B = [0]4

  print("A: ", geraVetor(A))
  print("B: ", geraVetor(B))
  print("União de A com B: ", uniao(A, B))

main()
