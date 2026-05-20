# Inteiros (int)
# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
# num_1 = int(input("Adicione um número inteiro: "))
# num_2 = int(input("Adicione outro número inteiro: "))
# sum_num = num_1 + num_2
# print(f"A soma de {num_1} e {num_2} é {sum_num}")

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
# num_user = int(input("Adicione um número: "))
# resto_div = num_user % 5
# print(f"O resto da divisão do número inserido pelo usuário {num_user} por 05 é {resto_div}")

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
# num_1 = int(input("Adicione um número inteiro: "))
# num_2 = int(input("Adicione outro número inteiro: "))
# multi_num = num_1 * num_2
# print(f"A multiplicação de ambos os números enviados pelo usuário é {multi_num}")

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
# num_1 = int(input("Adicione um número inteiro: "))
# num_2 = int(input("Adicione outro número inteiro: "))
# div_num = num_1 / num_2
# print(f"A divisão de ambos os números enviados pelo usuário é {div_num}")

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
# num_user = int(input("Envie um número para multiplicarmos o quadrado: "))
# quadrado_num = num_user ** 2
# print(f"O quadrado do número {num_user} é {quadrado_num}")

# Números de Ponto Flutuante (float)
# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
# num_1 = float(input("Digite um número: "))
# num_2 = float(input("Digite outro número: "))
# sum_num = num_1 + num_2
# print(f"A soma do número {num_1} com o número {num_2} é {sum_num}")

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
# num_1 = float(input("Digite um número: "))
# num_2 = float(input("Digite outro número: "))
# media_num = (num_1 + num_2) / 2
# print(f"A média do números é {media_num}")

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
# num_1 = int(input("Digite um número: "))
# pot = int(input("Digite um número para ser a potência: "))
# calc_pot = num_1 ** pot
# print(f"A potência do número {num_1} elevado a {pot} é {calc_pot}")

# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
# celc = float(input("Digite uma temperatura em célcius: "))
# conversao_celcius_fahrenheit = (celc * 1.8) + 32
# print(f"{celc}Cº convertidos para Fahrenheit é {conversao_celcius_fahrenheit}Fº")

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
# raio = float(input("Digite o valor do raio do circulo: "))
# calc_area = 3.14*(raio ** 2)
# print(f"A area do circulo é {calc_area:.2f}")

# Strings (str)
# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
# frase = input("Escreva uma frase: ")
# print(frase.upper())

# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
# nome = input("Digite seu primeiro nome: ")
# sobrenome = input("Digite seu sobrenome: ")

# print(nome.upper(), sobrenome.upper())
# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
# frase = input("Digite uma frase: ")
# print(frase.strip())

# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.

data = input("Digite uma data em formato 00/00/0000: ")
# Guarda os pedaços dentro de uma lista (array)
data_frac = data.split("/")
# Puxa os valores pela posição (índice)
print(f'Dia {data_frac[0]}, Mês {data_frac[1]}, Ano {data_frac[2]}')

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
 
#Booleanos (bool)
# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.