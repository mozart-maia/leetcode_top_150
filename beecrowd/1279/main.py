def checkBissex(year):
    if year % 400 == 0:
        return True
    if year % 4 == 0 and year % 100 != 0:
        return True
    return False

flag = False

while True:
    try:
        
        year = int(input())
        if flag:
            print()
        flagBi = False
        flagHulucu = False
        flagBuluku = False
        
        if checkBissex(year):
            flagBi = True
        
        if year % 55 == 0 and flagBi:
            flagBuluku = True
        
        if year % 15 == 0:
            flagHulucu = True
        
            
        if flagBi:
            print("This is leap year.")
        if flagHulucu:
            print("This is huluculu festival year.")       
        if flagBuluku:
            print("This is bulukulu festival year.")
        if (flagBi) or (flagBuluku) or (flagHulucu):
            pass
        else:            
            print("This is an ordinary year.")
        flag = True
        
        
        

    except EOFError:
        break





# This is leap year.

# This is leap year.
# This is huluculu festival year.

# This is huluculu festival year.

# This is an ordinary year.