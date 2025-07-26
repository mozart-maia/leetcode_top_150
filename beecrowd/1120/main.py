while True:
    try:
        c, line = input().split()
        if c == "0" and line == "0":
            break
        result = line.replace(c,"")
        if result == "":
            result = 0
        print(int(result))
    except EOFError:
        break