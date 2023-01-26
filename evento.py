arquivo = open("times.txt", "r")

time_a = arquivo.readline().rstrip()
time_b = arquivo.readline().rstrip()
maior = arquivo.readlines()[3]

print("JOGO")
print(time_a, "x", time_b)
print("Não perca esse evento!!")
print("O maior time do Brasil é", maior)

arquivo.close()

1# .rstrip() serve para "quebrar" o \n #
2# se der readlines dps de um readline o contador começará de novo, ou seja,(...)
 # (...) nesse caso o Corinthians é o elemento 5, porém virou o 3 por ter (...)
 # reiniciado #

