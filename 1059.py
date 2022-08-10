# 좋은 구간 미해결

cnt = int(input())
list = list(map(int, input().split()))
num = int(input())
list.sort()

last = int(min(list))
if num in list:
    print(0)
else:
    for i in list:
        if last <num < i:
            print((num-last-1)*(i-num)+(i-num-1))
        last = int(i) 


