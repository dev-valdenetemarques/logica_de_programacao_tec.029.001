# TODO:Crie um programa que receba do usuário o nome,a massa e
# a altura, e calcule seu IMC (Índice de Massa Corporal).
# Após mostrar o IMC, o programa deve informar de acordo com o
# valor do seu IMC:
# - IMC < 18.5: "Usuário está abaixo do peso"
# - IMC < 25: "Usuário está no peso ideal"
# - IMC < 30: "Usuário está acima do peso"
# - IMC < 35: "Usuário estaá obeso"
# - IMC < 40: "Usuário está com obesidade nivel 2"
# - Se não estiver em nenhum dos casos acima:
# - "Usuário está com obesidade morbida"
# NOTE: inc = massa/(altura**2)

nome = input("informe seu nome: ")
massa = float(input("informe sua massa (kg): "))
altura = float(input("informe sua altura (m): "))

icm = massa / (altura ** 2)
print(f"Seu IMC é: {icm:.2f}")
if icm < 18.5:
    print("usuário está abaixo do peso")
elif icm < 25:
    print("usuário está no peso ideal")
elif icm < 30:
    print("usuário está acima do peso")
elif icm < 35:
    print("usuário está obeso")
elif icm < 40:
    print("usuário esta com obesidade nível 2")
else:
    print("usuário está com obesidade morbida")
