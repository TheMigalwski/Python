# exerc 3 - fatorial
resposta = "S"
while resposta == "S":

    thiago = int(input(" Digite um número para fatorial: " ))

    fat = 1
    for i in range(1, thiago + 1,1):
        fat= fat * i
    print("O fatorial de ", thiago, " ", fat)
    resposta = str(input("Deseja continuar fatorando? (S/N): ")).upper()
print("Fim")
