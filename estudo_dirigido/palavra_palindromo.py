palavra = input("Digite uma palavra ")
print(f'A palavra é um palíndromo' if palavra == palavra[::-1] else f'Essa palavra não é um palíndromo')