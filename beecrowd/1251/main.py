first = True
while True:
    try:
        mapa = {}
        chars = input()
        for e in chars:
            asci = ord(e)
            if asci in mapa:
                mapa[asci] += 1
            else:
                mapa[asci] = 1
        if first:
            first = False
        else:
            print()
        lista = []
        for k,v in mapa.items():
            lista.append((k,v))
        ord_by_char = sorted(lista, key=lambda x: x[0], reverse=True)
        ord_by_ocorrences = sorted(ord_by_char, key=lambda x: x[1])
        for e in ord_by_ocorrences:
            print(e[0],e[1])        
    except EOFError:
        break
    