"""Três amigos, Carlos, André e Felipe, decidiram rachar igualmente a conta em um bar.
Faça um programa para ler o valor total da conta e
imprimir quanto cada um deve pagar, mas faça com que Carlos e André não paguem centavos. 
Por exemplo: uma conta de R$101,53 resulta em R$33,00 para Carlos, R$33,00
para André e R$ 35,53 para Felipe.
"""

carlos = float(input("digite o valor gasto pelo Carlos: "))
andre = float(input("digite o valor gasto pelo André: "))
felipe =  float(input("digite o valor gasto pelo Felipe: "))

total3 = carlos  + andre + felipe
print("\nO valor da conta dos amigos foi: ", total3)

total_carlos = ( carlos  + andre + felipe) // 3
print("\nO pagamento Carlos é : R$ %.2f" %total_carlos)

total_andre = ( carlos  + andre + felipe) // 3
print("\nO pagamento André é : R$ %.2f" %total_andre)

total_felipe = total3 - total_carlos - total_andre
print("\nO pagamento Felipe é : R$ %.2f" %total_felipe)


valor_total = float(input("Insira o valor total da conta:"))

divisao = valor_total//3

resto = valor_total - (divisao * 3)

parte_do_felipe = divisao + resto

print(f"Valores de pagamentos individuais:\n")
print(f"André:R$",format(divisao,".2f"),"reais\nCarlos:R$",format(divisao,".2f"),"reais")
print("Felipe:R$",format(parte_do_felipe,".2f"),"reais")
