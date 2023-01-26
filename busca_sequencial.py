import random 

def gerarVetorOrdenado(n):
    vetor = [0]*n
    for i in range(n):
        vetor[i]=random.randint(1,20)
    vetor.sort()
    return vetor

def buscaSequencial1(vetor,x):
    cont=0
    for i in range(len(vetor)):
        cont+=1 #conta quantidade de comparações
        if vetor[i] == x:
            print("quantidade de passos--> ",cont) )#se achou!
            return i
    print("quantidade de passos--> ",cont) )#se não achou!
    return -1;

def buscaSequencial2(vetor,x):
    k=0
    while k < len(vetor):
        if vetor[k] == x:
            return k
        k+=1
    return -1;

def buscaSequencialOrdenada(vetor,x):    
    for i in range(len(vetor)):        
        if vetor[i] == x:
            print("quantidade de passos--> ",i+1)
            return i
        else:
            if x < vetor[i]:
                print("quantidade de passos--> ",i+1)
                return -1
    print("quantidade de passos--> ",i+1)    
    return -1


vetor=[5,16,17,28,91,100]
print(vetor)
print(buscaSequencialOrdenada(vetor,17))
print(buscaSequencialOrdenada(vetor,30))
print(buscaSequencialOrdenada(vetor,100))
