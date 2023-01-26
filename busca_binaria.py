import random

def buscaBinaria(vetor,x):
    cont=0
    low=0
    high=len(vetor)-1
    while low <= high:
        cont += 1
        mid = (low + high)//2
        if vetor[mid] == x:
            print("quantidade de passos--> ",cont)
            return mid
        else:
            if vetor[mid] < x:
                low = mid + 1
            else:
                high = mid - 1
    print("quantidade de passos--> ",cont)
    return -1

vetor=[5,6,7,8,9,10]
print(vetor)
print(buscaBinaria(vetor,5))
print(buscaBinaria(vetor,7))
print(buscaBinaria(vetor,10))
