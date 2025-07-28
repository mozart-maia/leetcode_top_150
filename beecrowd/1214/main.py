

n = int(input())
for i in range(n):
    nlist = list(map(int, input().split()))
    students = nlist[0]
    nlist = nlist[1:]
    media = sum(nlist) / students
    students_above = 0
    for e in nlist:
        if e > media:
            students_above += 1
    print("{:.3f}%".format(students_above/students*100))
