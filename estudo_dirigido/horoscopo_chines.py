def calcular_signo():
    ano_nascimento = int(input("Digite o ano de nascimento: "))
    signos_chineses = ["Rato", "Boi", "Tigre", "Coelho", "Dragão", "Serpente", "Cavalo", "Cabra", "Macaco", "Galo", "Cachorro", "Porco"]
    ano_base = 1900  
    indice_signo = (ano_nascimento - ano_base) % 12
    return signos_chineses[indice_signo]

signo = calcular_signo()
print(f"Seu signo chinês é {signo}")