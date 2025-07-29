n = int(input())
fila1 = input().split()
fila1_clone = fila1.copy()
m = int(input())
fila2 = input().split()
for each in fila2:
    if each in fila1_clone:
        fila1_clone.remove(each)



for i in range(len(fila1_clone)-1):
    print(fila1_clone[i],end=" ")
print(fila1_clone[-1], end="\n")
