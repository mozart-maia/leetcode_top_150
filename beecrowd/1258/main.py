first = True
while True:
    n = int(input())
    if n == 0:
        break
    lista = []
    if first:
        first = False
    else:
        print()


    for i in range(n):
        nome = input()
        cor, tamanho = input().split()
        
        lista.append((cor, nome, tamanho))
        
    ord_nome = sorted(lista, key=lambda a: a[1])
    ord_tamanho = sorted(ord_nome, key=lambda b: b[2], reverse=True)  
    ord_cor = sorted(ord_tamanho, key=lambda a: a[0])  
    for e in ord_cor:
        print(e[0],e[2],e[1])
