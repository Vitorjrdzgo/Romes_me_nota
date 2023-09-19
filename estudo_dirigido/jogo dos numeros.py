import random
Random_number = random.randint(1,11)

while True:
    adivinhar_numero = int(input("Digite um número de 1 a 10 "))
    if adivinhar_numero <1 or adivinhar_numero > 11:
        print("Insira um número válido!")
        continue
    break

if adivinhar_numero == Random_number:
    print("Você acertou!")
else:
    print("Você errou!")
