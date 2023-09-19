numero = int(input("Digite um número "))
print(f"O número {numero} é divisivel por 3 e por 5." if numero % 5 == 0 and numero % 3 == 0 else f'O número não é divisivel por 3 e por 5.')