def lista():
    lista = []
    while True:

        frutas = input("Digite uma fruta ou 'sair' para sair ")
        frutasmin = frutas.lower()
        if frutas == 'sair':
             print('Voce saiu.\nOs objetos que foram adicionados a lista são:')
             print(lista)
             exit()
        lista.append(frutasmin)
        print('A fruta foi adiciona a lista.')

lista()
