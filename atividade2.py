def qtd_caracteres():
    palavra = input("Digite uma palavra: ")
    return len(palavra)

print("A palavra digitada contém " + str(qtd_caracteres()) + " caracteres.")