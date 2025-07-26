def checkFrequency(frequency):
    sum = 0
    records = len(frequency)
    for e in frequency:
        if e == "M":
            records -= 1
        if e == "P":
            sum += 1
    if sum / records < 0.75:
        return True
    return False

while True:
    try:
        n = int(input())
        for i in range(n):
            nstudents = int(input())
            names = input().split()
            frequencies = input().split()
            reprovados = []
            for j in range(nstudents):
                name = names[j]
                frequency = frequencies[j]
                if checkFrequency(frequency):
                    reprovados.append(name)
                

            for e in range(len(reprovados)-1):
                print(reprovados[e],end=" ")
            if len(reprovados) > 0:
                print(reprovados[-1])
            else:
                print()

                
    except EOFError:
        break