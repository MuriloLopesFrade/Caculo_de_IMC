#Obtendo as informações
peso = float(input("Digite o seu peso em quilogramas:"))
altura = float(input("Digite a sua altura em metros:"))

#Calculando o IMC
imc = peso / (altura * altura)

#Classificando o IMC
if (imc < 16):
    print(f"O valor do IMC é: {imc:.1f}")
    print("Magreza grau III")
elif (imc < 16.9):
    print(f"O valor do IMC é: {imc:.1f}")
    print("Magreza grau II")
elif (17 <= imc <= 18.4):
    print(f"O valor do IMC é: {imc:.1f}")
    print("Magreza grau I")
elif (18.5 <= imc <= 24.9):
    print(f"O valor do IMC é: {imc:.1f}")
    print("Peso Normal")
elif (25 <= imc < 29.9):
    print(f"O valor do IMC é: {imc:.1f}")
    print("Pré-obesidade")
elif (30 <= imc < 34.9):
    print(f"O valor do IMC é: {imc:.1f}")
    print("Obesidade moderada (grau I)")
elif (35 <= imc < 39.9):
    print(f"O valor do IMC é: {imc:.1f}")
    print("Obesidade severa (grau II)")
else:
    print(f"O valor do IMC é: {imc:.1f}")
    print("Obesidade muito severa (grau III)")
