def substituir_vogal():
    texto = input("Digite uma palavra: ")
    return texto.lower().replace('a', '*').replace('e', '*').replace('i', '*').replace('o', '*').replace('u', '*')
    
print(substituir_vogal())