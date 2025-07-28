def checkPrimo(number):
    sqrt = int(number**(1/2)+1)
    if number == 2:
        return True
    if number == 1:
        return False
    for i in range(2,sqrt):
        if number % i == 0:
            return False    
    return True

char_primos = "2357"

while True:
    try:
        listn = input().split()
        for each in listn:
            number = each
            isPrimo = checkPrimo(int(number))
            if isPrimo:
                notSuper = False
                for char in number:
                    if char not in char_primos:
                        notSuper = True
                        break
                if notSuper:
                    print("Primo")
                    continue
                else:
                    print("Super")                
            else: 
                print("Nada")

    except EOFError:
        break

