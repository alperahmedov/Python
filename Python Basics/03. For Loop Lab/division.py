n = int(input())
p1 = p2 = p3 = 0

for i in range(0, n):
    inp = int(input())
    if inp % 4 == 0:
        p3 += 1
    if inp % 2 == 0:
        p1 += 1
    if inp % 3 == 0:
        p2 += 1

print(f"{p1 / n * 100:.2f}%\n{p2 / n * 100:.2f}%\n{p3 / n * 100:.2f}%")
