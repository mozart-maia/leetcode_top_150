def checkPassword(password):
    numeros = "1234567890"
    minusculas = "abcdefghijklmnopqrstuvwxyz"
    maiusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    flagMaiuscula = False
    flagMinuscula = False
    flagNumero = False
    flagTamanho = False

    if len(password) >= 6 and len(password) <= 32:
        flagTamanho = True

    for e in password:
        if e in numeros:
            flagNumero = True
            continue
        if e in minusculas:
            flagMinuscula = True
            continue
        if e in maiusculas:
            flagMaiuscula =  True
            continue
        # print("caractere desconhecido encontrado: ",e)
        return False
        break

    return (flagMaiuscula and flagMinuscula and flagNumero and flagTamanho)

while True:
    try:
        line = input()
        if checkPassword(line):
            print("Senha valida.")
        else:
            print("Senha invalida.")
    except EOFError:
        break