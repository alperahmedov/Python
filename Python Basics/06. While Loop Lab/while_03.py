# Напишете програма, която чете цяло число от конзолата и на всеки следващ ред цели числа, докато тяхната сума стане
# по-голяма или равна на първоначалното число. След приключване на четенето да се отпечата сумата на въведените числа.

start_number = int(input())
sum = 0
while sum < start_number:
    number = int(input())
    sum += number
else:
    print(sum)

