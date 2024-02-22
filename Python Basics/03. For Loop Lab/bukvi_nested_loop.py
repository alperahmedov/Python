K = int(input())  ## 0-8
L = int(input())  # 9-0
M = int(input())  ## 0-8
N = int(input())  # 9-0
count = 0
halt = False
if L % 2 == 0:
    L += 1
if N % 2 == 0:
    N += 1

if K % 2 != 0:
    K += 1
if M % 2 != 0:
    M += 1

for k in range(K, 9, 2):
    if halt:
        break
    for l in range(9, L - 1, -2):
        if halt:
            break
        for m in range(M, 9, 2):
            if halt:
                break
            for n in range(9, N - 1, -2):
                if int(str(k) + str(l)) != int(str(m) + str(n)):
                    print(f"{k}{l} - {m}{n}")
                    count += 1
                    if count >= 6:
                        halt = True
                        break
                else:
                    print("Cannot change the same player.")