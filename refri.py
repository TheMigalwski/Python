

lata = int(input("Digite quantidade de latas compradas:\n"));
garrafa_600 = int(input("Digite quantidade de garrafas de 600ml:\n"));
garrafa_2 = int(input("Digite quantidade de garrafas 2L:\n"));

v_total = (lata*0.35) + (garrafa_600*0.6) + (garrafa_2*2);

print("\nVocê comprou, no total,", v_total,"litros");
