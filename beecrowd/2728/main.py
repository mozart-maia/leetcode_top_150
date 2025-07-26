def checkCobol(line):
    words = line.split("-")
    letters = words[0][0].lower() + words[0][-1].lower()
    if "c" not in letters:
        return False
    letters = words[1][0].lower() + words[1][-1].lower()
    if "o" not in letters:
        return False
    letters = words[2][0].lower() + words[2][-1].lower()
    if "b" not in letters:
        return False
    letters = words[3][0].lower() + words[3][-1].lower()
    if "o" not in letters:
        return False
    letters = words[4][0].lower() + words[4][-1].lower()
    if "l" not in letters:
        return False
    return True

while True:
    try:
        line = input()
        if checkCobol(line):
            print("GRACE HOPPER")
        else:
            print("BUG")
                
    except EOFError:
        break