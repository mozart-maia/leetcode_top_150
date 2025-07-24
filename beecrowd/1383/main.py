n = int(input())

for i in range(n):
    line = input().split()
    print(line)
    line.sort(reverse=True)
    print(line)
