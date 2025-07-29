n = int(input())
for i in range(n):
    l_words = input().split()
    result = sorted(l_words, key=lambda a: len(a), reverse=True)
    for j in range(len(result)-1):
        print(result[j],end=" ")

    print(result[-1],end="\n")
