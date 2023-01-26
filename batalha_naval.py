import random as rd

def matriz():
    y,x= rd.randint(0,9),rd.randint(0,9)
    r = rd.randint(1,2)
    return y,x,r
 
def matriz2():
    y,x,r = int(input("Posição X: ")), int(input("Posição Y: ")),int(input("Rotação (1=vertical;2=horizontal): ")) 
    return y,x,r

def matriz3():
    a = [0]*10
    for i in range(10):
        a[i] = [0]*10
    return a

def matrizP(M):
    fM = M
    for i in range(10):
        for j in range(10):
            if fM[i][j] == 0:
                fM[i][j] = '.'
            print(fM[i][j],end=" ")
        print()
    for i in range(10):
        for j in range(10):
            if fM[i][j] == '.':
                fM[i][j] = 0

def foraGrid(M,tipo,y,x,r):
    size= len(M)
    if tipo == "P":
        if r == 1:
            for i in range(5):
                if(y+i) >= size or x >= (size):
                    return True
        elif r == 2:
            for i in range(5):
                if (y) >= size or (x+i) >= size:
                    return True
            
    elif tipo == "E":
        if r == 1:
            for i in range(4):
                if(y+i) >= size or x >= (size):
                    return True
        elif r == 2:
            for i in range(4):
                if (y) >= size or (x+i) >= size:
                    return True

    elif tipo == "C":
        if r == 1:
            for i in range(3):
                if(y+i) >= size or x >= (size):
                    return True
        elif r == 2:
            for i in range(3):
                if (y) >= size or (x+i) >= size:
                    return True
            
    elif tipo == "S":
        if r == 1:
            for i in range(2):
                if(y+i) >= size or x >= (size):
                    return True
        elif r == 2:
            for i in range(2):
                if (y) >= size or (x+i) >= size:
                    return True
    return False

def verifica(M,tipo,y,x,r):
    if tipo == "P":
        if r == 1:
            for i in range(5):
                if M[y+i][x] != 0:
                    return True
        elif r == 2:
            for i in range(5):
                if M[y][x+i] != 0:
                    return True
            
    elif tipo == "E":
        if r == 1:
            for i in range(4):
                if M[y+i][x] != 0:
                    return True
        elif r == 2:
            for i in range(4):
                if M[y][x+i] != 0:
                    return True

    elif tipo == "C":
        if r == 1:
            for i in range(3):
                if M[y+i][x] != 0:
                    return True
        elif r == 2:
            for i in range(3):
                if M[y][x+i] != 0:
                    return True
            
    elif tipo == "S":
        if r == 1:
            for i in range(2):
                if M[y+i][x] != 0:
                    return True
        elif r == 2:
            for i in range(2):
                if M[y][x+i] != 0:
                    return True
    return False

def barco(M,tipo,y,x,r):
    if tipo == "P":
        if r == 1:
            for i in range(5):
                M[y+i][x] = tipo
        elif r == 2:
            for i in range(5):
                M[y][x+i] = tipo
            
    elif tipo == "E":
        if r == 1:
            for i in range(4):
                M[y+i][x] = tipo
        elif r == 2:
            for i in range(4):
                M[y][x+i] = tipo

    elif tipo == "C":
        if r == 1:
            for i in range(3):
                M[y+i][x] = tipo
        elif r == 2:
            for i in range(3):
                M[y][x+i] = tipo
            
    elif tipo == "S":
        if r == 1:
            for i in range(2):
                M[y+i][x] = tipo 
        elif r == 2:
            for i in range(2):
                M[y][x+i] = tipo
    else:
        print("Tipo nao reconhecido durante placement")
        
    return M

def conv(i):
    tipo = ""
    if i == 0:
        tipo = 'P'
    elif i == 1:
        tipo = 'E'
    elif i == 2:
        tipo = 'C'
    elif i == 3: 
        tipo = 'S'
    else:
        print("Conversao erro")
    return tipo

def checkBarco(M):
    i = 0
    while i <= 3:
        print(f"Posicione o barco tipo {conv(i)}.")
        tipo = conv(i)
        x,y,r = matriz2()
        if foraGrid(M,tipo,y,x,r)== False:
            if verifica(M,tipo,y,x,r) == False:
                M = barco(M,tipo,y,x,r)
                i += 1
            else:
                print("Posicao considerada ocupada, considere outra posicao.")
        else:
            print("Posicao fora do grid.")
        matrizP(M)

def main():
    print("FASE 1 (INPUT)\n")
    M = matriz3()
    print("p = Porta aviões\ne = Escudeiro\nc = Cruzador\ns = Submarino\nPosições vão de 0 a 9.\n")
    checkBarco(M)
    print("\nMatriz  finalizada!")
    matrizP(M)
    print("\n-----programa-finalizado-----\n")

def inimigo(M):
    i = 0
    while i <= 3:
        tipo = conv(i)
        x,y,r = matriz()
        if foraGrid(M,tipo,y,x,r)== False:
            if verifica(M,tipo,y,x,r) == False:
                M = barco(M,tipo,y,x,r)
                i += 1
                
def acerto(M,Mf,x,y):
    status = ''
    if M[y][x] != 0:
        status = "Success"
        Mf[y][x] = "X"
    else:
        status = "Failure"
        Mf[y][x] = "o"
    return status

def tiro(M,Mf):
    print('Entenda que "O" indica falha e "X" indica acerto')
    tentativas = 20
    i= 0
    while i <= (tentativas):
        x,y = int(input("X: ")), int(input("Y: "))
        print(acerto(M,Mf,x,y))
        if acerto(M,Mf,x,y) == "Failure":
            i +=1
        print(f"Tentativas: {tentativas-i}")
        matrizP(Mf)

def main2():
    print("FASE 2\n")
    M = matriz3()
    Mf = matriz3()
    inimigo(M)
    tiro(M,Mf)
    print("\nMatriz secreta:")
    matrizP(M)
    print("\n-----programa-finalizado-----\n")

main()
main2()
