n = int(input())
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0
for _ in range(n):
    current_number = int(input())

    if current_number < 200:
        p1 += 1
    elif 200 <= current_number <= 399:
        p2 += 1
    elif 400 <= current_number <= 599:
        p3 += 1
    elif 600 <= current_number <= 799:
        p4 += 1
    elif current_number >= 800:
        p5 += 1
p1 = p1 / n * 100
p2 = p2 / n * 100
p3 = p3 / n * 100
p4 = p4 / n * 100
p5 = p5 / n * 100
print(f"{p1:.2f}%")
print(f"{p2:.2f}%")
print(f"{p3:.2f}%")
print(f"{p4:.2f}%")
print(f"{p5:.2f}%")
# p1 = 12 / 20 * 100 = 60.00%
# p2 = 2 / 20 * 100 = 10.00%
# p3 = 1 / 20 * 100 = 5.00%
# p4 = 3 / 20 * 100 = 15.00%
# p5 = 2 / 20 * 100 = 10.00%
