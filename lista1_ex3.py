#exercício 3
salarioMinimo = float(input("Digite o salário:\n"));
aguaConsumida = float(input("Digite o seu consumo de água:\n"));
perc = 2 * (aguaConsumida/1000);
contaDAgua = (perc/100) * salarioMinimo;
print("O valor da sua conta de água é:", contaDAgua);
desc = contaDAgua * 0.85;
print("O valor da sua conta d'água, com desconto, é:", desc);

