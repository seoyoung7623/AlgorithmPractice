M = int(input())
N = int(input())
total = 0
min_num = 0
toggle = False

for i in range(M,N+1):
    if i == 1:
        continue
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        if not toggle:
            min_num = i
            toggle = True
        total += i

if total == 0:
    print(-1)
else:
    print(total)
    print(min_num)
