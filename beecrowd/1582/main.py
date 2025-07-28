def checkPitagorica(lista):
    if (lista[0] ** 2) + (lista[1] ** 2) == (lista[2] **2):
        return True
    return False

def checkMdc(lista):
    mini = lista[0]
    while True:
        if mini == 1:
            return True
        if (lista[0] % mini ==0) and (lista[1] % mini ==0) and (lista[2] % mini ==0):
            return False
        mini -= 1 

while True:
    try:
        lista = list(map(int, input().split()))
        lista.sort()
        flagPitagoras = checkPitagorica(lista)
        if flagPitagoras:
            if checkMdc(lista):
                print("tripla pitagorica primitiva")
            else:
                print("tripla pitagorica")
        else:
            print("tripla")
    except EOFError:
        break


# tripla pitagorica
# tripla pitagorica primitiva
# tripla