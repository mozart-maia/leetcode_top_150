while True:
    try:
        n = int(input())
        botas = {}
        pares = 0
        for i in range(n):
            bota = input()
            pe = bota[len(bota)-1]
            if pe == "E":
                pe = "D"
            else:
                pe = "E"
            pe_oposto = bota[:-1]+pe

            if pe_oposto in botas and botas[pe_oposto] > 0:

                botas[pe_oposto] -= 1
                pares += 1
            else:
                if bota in botas:
                    botas[bota] += 1
                else:
                    botas[bota] = 1

        print(pares)        
    except EOFError:
        break