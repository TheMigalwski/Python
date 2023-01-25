#exercício 5 && 6 - fruta
fruitName = input("Digite o nome de uma fruta:\n");
precoFruit = float(input("Digite o preço da fruta:\n"));
vegName = input("\nAgora de uma verdura:\n");
precoVeg = float(input("Agora o preço da verdura:\n"));
legName = input("\nPra finalizar, o nome de um legume:\n");
precoLeg = float(input("Por fim, o preço do legume:\n"));
print("\nAqui estão os nomes de uma fruta, uma verdura e um legume:");
print("Fruta é", fruitName,"seu preço é: R$%.2f" %precoFruit);
print("\nVerdura =", vegName,"seu preço é: R$.2f" %precoVeg)
print("\nLegume = ", legName,"seu preço é: R$.2f" %precoLeg);
