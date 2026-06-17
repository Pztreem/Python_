import os
os.system ('cls')

peso = float(input("Coloque seu peso (kg): "))
altura = float(input("Coloque sua altura (m): "))

imc = peso / (altura ** 2)

print(f"\nSeu IMC é: {imc:.2f}")

if imc < 18.5:
    print("Resultado: Abaixo do peso")
elif imc < 25:
    print("Resultado: Peso normal")
elif imc < 30:
    print("Resultado: Sobrepeso")
elif imc < 35:
    print("Resultado: Obesidade grau I")
elif imc < 40:
    print("Resultado: Obesidade grau II")
else:
    print("Resultado: Obesidade grau III")
