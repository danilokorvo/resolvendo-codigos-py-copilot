# Saudação inicial
print("Bem-vindo(a) ao Calculador de IMC!")

# Entrada dos dados
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

# Cálculo do IMC
imc = peso / (altura ** 2)

# Exibindo o resultado com formatação
print(f"Seu IMC é: {imc:.2f}")

# Classificação do IMC
if imc < 18.5:
    print("Classificação: Abaixo do peso")
elif 18.5 <= imc < 24.9:
    print("Classificação: Peso normal")
elif 25 <= imc < 29.9:
    print("Classificação: Sobrepeso")
elif 30 <= imc < 34.9:
    print("Classificação: Obesidade grau I")
elif 35 <= imc < 39.9:
    print("Classificação: Obesidade grau II")
else:
    print("Classificação: Obesidade grau III")