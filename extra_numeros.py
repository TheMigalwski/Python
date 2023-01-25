'''
7/5 = 1.40
7//5 = 1
7%5 = 2
7**5 = 16807
'''
#extra
import math

num1 = int(input("Digite um número inteiro\n"));
num2 = int(input("Digite um número inteiro\n"));

div = num1/num2;
print("\nO resultado do operador / é:", div);

barra_barra = num1//num2;
print("\nO resultado do operador // é:", barra_barra);

resto_divisao = num1%num2;
print("\nO resultado do operador% é:", resto_divisao);

elevado = num1**num2;
print("\nO resultado do operador **(elevado) é:", elevado);

elevado_func = math.pow(num1, num2);
print("\nO resultado do operador **(elevado com função) é: %.0d"%elevado_func);

elevado_func = math.pow(num1, num2);
print("\nO resultado do operador **(elevado com função) é: ", format(elevado_func,".0d"));
