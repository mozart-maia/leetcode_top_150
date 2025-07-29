def checkIntersec(lista1, lista2):
    return len(set(lista1) & set(lista2))

def checkUnion(lista1, lista2):
    lista_set = set(lista1 + lista2)
    return len(lista_set)

instancias = int(input())

for i in range(instancias):
    conjuntos = []
    c = int(input())
    for each in range(c):
        lista = input().split()
        conjuntos.append(lista[1:])
    ops = int(input())
    for i in range(ops):
        op, x, y = input().split()
        x = int(x)
        y = int(y)
        if op == "1":
            print(checkIntersec(conjuntos[x-1], conjuntos[y-1]))
        if op == "2":
            print(checkUnion(conjuntos[x-1], conjuntos[y-1]))
        