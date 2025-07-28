memo = {1: 2}


total = 2

for i in range(2,65):
    total *= 2
    memo[i] = total

n = int(input())
for i in range(n):
    number = int(input())
    print(int(memo[number]/12000),"kg")