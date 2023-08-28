def juntar_nome():
    nome = input("Digite seu nome completo: ")
    frag_nome = nome.split()
    nome_parte = frag_nome[0]
    sobrenome = " ".join(nome_parte[1:])
    nome_completo = nome.upper()
    tamanho_nome = len(nome)
    print(nome.lower())
    print("Seu nome contém: "+ str(tamanho_nome) + " caracteres.")

print(juntar_nome())