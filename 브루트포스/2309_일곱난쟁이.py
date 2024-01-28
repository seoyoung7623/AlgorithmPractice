# 2309 일곱 난쟁이
import sys
input = sys.stdin.readline

lst = list(int(input()) for _ in range(9))
lst.sort()
min_num = 0
max_num = 8
while True:
    answer = sum(lst) - lst[min_num] - lst[max_num]
    if answer > 100:
        min_num += 1
    elif answer < 100:
        max_num -= 1
    else:
        break
for i in range(9):
    if i == min_num or i == max_num:
        continue
    else:
        print(lst[i])