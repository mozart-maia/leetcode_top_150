def checkPrimo(number):
    sqrt = int(number**(1/2)+1)
    if number == 2:
        return True
    for i in range(2,sqrt):
        if number % i == 0:
            return False    
    return True

n = int(input())

for i in range(n):
    number = int(input())

    if (checkPrimo(number)):
        print("Prime")
    else:
        print("Not Prime")