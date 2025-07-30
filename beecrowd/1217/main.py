n = int(input())

value = 0.0
frutas = []
counter = 0
for i in range(n):
    value += float(input())
    f_line = input().split()
    fruta_iter = []
    counter += 1
    for e in f_line:
        frutas.append(e)
        fruta_iter.append(e)
    print("day {}: {} kg".format(counter,len(fruta_iter)))
print("{:.2f} kg by day".format(len(frutas)/n))
print("R$ {:.2f} by day".format(value/n))