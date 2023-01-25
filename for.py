cont = 0
ac = 0

for number in range(1, 100, 2):
    print(number, end = " ")
    cont = cont + 1 
    ac = ac + number
print("\nA quantidade de números ímpares: ", cont)
print("\nA somatória dos números ímpares: ", ac)
