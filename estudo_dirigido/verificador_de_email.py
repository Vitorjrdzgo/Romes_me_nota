email_do_usuario = input("Digite seu e-mail: ")

def email_valido(email):
    if '@' in email:
        return True
    elif " " in email:
        return False
    elif "." in email:
        return True
    else:
        return False
    
print(email_valido(email_do_usuario))