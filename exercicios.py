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

# data = input("Digite uma data em formato 00/00/0000: ")
# # Guarda os pedaços dentro de uma lista (array)
# data_frac = data.split("/")
# # Puxa os valores pela posição (índice)
# print(f'Dia {data_frac[0]}, Mês {data_frac[1]}, Ano {data_frac[2]}')

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
# frase_1 = input("Digite algo: ")
# frase_2 = input("Digite algo: ")
# frase_completa = frase_1 + " " + frase_2
# print(frase_completa)
 
#Booleanos (bool)
# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
# entrada_1 = input("Digite True ou False:")
# entrada_2 = input("Digite True ou False:")
# # Formatando entrada de dados
# formatado_1 = entrada_1.strip().capitalize()
# formatado_2 = entrada_2.strip().capitalize()
# # Aplicando os valores para booleano
# booleano_1 = formatado_1 == "True"
# booleano_2 = formatado_2 == "True"
# #Criando a lógica
# result = booleano_1 and booleano_2
# print(result)

# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
# entrada_1 = input("Digite True ou False: ")
# entrada_2 = input("Digite True ou False: ")
# #Limpando entrada dos dados
# formatado_1 = entrada_1.strip().capitalize()
# formatado_2 = entrada_2.strip().capitalize()
# #Transformando em booleano
# booleano_1 = formatado_1 == "True"
# booleano_2 = formatado_2 == "True"
# #Criando a lógica
# result = booleano_1 or booleano_2

# print(result)

# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
# entrada = input("Digite um valor booleano 'True' ou 'False': ")
# #Formatando o valor de entrada
# formatado = entrada.strip().capitalize()
# #Transformando em booleano
# booleano = formatado == "True"
# #Imprimindo valor reverso
# print(not booleano)

# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
# valor1 = int(input("Digite um valor: "))
# valor2 = int(input("Digite outro valor: "))

# print('Se o valor for igual irá aparecer "True", se não irá aparecer "False"')
# comparacao = valor1 == valor2
# print(comparacao)

# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
# valor1 = int(input("Digite um valor: "))
# valor2 = int(input("Digite outro valor: "))

# print('Se o valor for diferente irá aparecer "True", se não irá aparecer "False"')
# comparacao = valor1 != valor2
# print(comparacao)

# Exercícios extras
# Exercício 21: Conversor de Temperatura
# Escreva um programa que converta a temperatura de Celsius para Fahrenheit. O programa deve solicitar ao usuário a temperatura em Celsius e, 
# utilizando try-except, garantir que a entrada seja numérica, tratando qualquer ValueError. Imprima o resultado em Fahrenheit ou uma mensagem de erro se a entrada não for válida.

# entrada = input("Digite a temperatura em Celsius: ")

# try:
#     #Tenta converter a entrada para float
#     celsius = float(entrada)
#     #Aplica a formula de conversão
#     fahrenheit = (celsius * 1.8) + 32
#     #Exibe o resultado formatado
#     print(f"A temperatura de {celsius}Cº equivale a {fahrenheit:.1f}F.")
# except ValueError:
#     #Trata o erro caso ele não seja um número válido
#     print("Erro: Por favor, insira um valor numérico valido (Ex: 25 ou 23.5).")

# Exercício 22: Verificador de Palíndromo
# Crie um programa que verifica se uma palavra ou frase é um palíndromo (lê-se igualmente de trás para frente, desconsiderando espaços e pontuações). 
# Utilize try-except para garantir que a entrada seja uma string. Dica: Utilize a função isinstance() para verificar o tipo da entrada.

# entrada = input("Digite uma frase ou palavra: ")

# try:
#     #Verificar se a entrada é vazia
#     if entrada.strip() == "":
#         raise ValueError("Você não pode deixar o campo vazio")
#     #Verificar se são apenas números
#     if entrada.isdigit():
#         raise ValueError("Não é possivel digitar apenas números!")
#     #Tratar os dados
#     dados_limpos = entrada.replace(" ", "").lower()
#     #inverter os dados
#     texto_invertido = dados_limpos[::-1]
#     #comparar os dados
#     if dados_limpos == texto_invertido:
#         print("É um palíndromo")
#     else:
#         print("Não é um palíndromo")
# except ValueError as erro:
#     print(f"Erro de validação: {erro}")

# Exercício 23: Calculadora Simples
# Desenvolva uma calculadora simples que aceite duas entradas numéricas e um operador (+, -, *, /) do usuário. 
# Use try-except para lidar com divisões por zero e entradas não numéricas. Utilize if-elif-else para realizar a 
# operação matemática baseada no operador fornecido. Imprima o resultado ou uma mensagem de erro apropriada.

# operadores_validos = ["+", "-", "*", "/"]

# try:
#     num1 = float(input("Digite um número: "))
#     operador = input("Digite um operador (+, -, *, /): ").strip()
#     #Validação do operador
#     if operador not in operadores_validos:
#         raise ValueError("Operador invalido use apenas + - * ou /.")
#     num2 = float(input("Digite um segundo número: "))

#     #Executando operações
#     if operador == "+":
#         resultado = num1 + num2
#     elif operador == "-":
#         resultado = num1 - num2
#     elif operador == "*":
#         resultado = num1 * num2
#     elif operador == "/":
#         resultado = num1 / num2
#     print(f"O resultado de {num1} {operador} {num2} é = {resultado}")

# except ValueError as erro_num:
#     print(f"Erro de entrada: {erro_num}")
# except ZeroDivisionError:
#     print("Erro matemático, não é possivel dividir por zero!")

# Exercício 24: Classificador de Números
# Escreva um programa que solicite ao usuário para digitar um número. Utilize try-except para assegurar que a entrada seja numérica e 
# utilize if-elif-else para classificar o número como "positivo", "negativo" ou "zero". Adicionalmente, identifique se o número é "par" ou "ímpar".


try:
    numero = int(input("Digite um número inteiro: "))
    if numero > 0:
        print("É um número positivo")
    elif numero < 0:
        print("É um número negativo")
    else:
        print("O número é zero")
    if numero % 2 == 0:
        print("Número é par")
    else: 
        print("Número é impar")
except ValueError:
    print("Digite um número válido")