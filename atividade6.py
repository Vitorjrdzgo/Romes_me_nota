def nome_composto():
    nome = input('digite seu nome: ')
    sobrenome = input('digite seu sobrenome: ')
    return nome.upper(), sobrenome.lower()

print(nome_composto())