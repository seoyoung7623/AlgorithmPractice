# 좋은 구간
cnt = int(input())
list = list(map(int, input().split()))
num = int(input())
list.append(0) # 리스트의 값들보다 작은 num 이 있을수 있기때문에 추가
list.sort()

last = int(min(list))
if num in list:
    print(0)
else:
    for i in list:
        if last <num < i:
            print((num-last-1)*(i-num)+(i-num-1))
            break
        last = int(i) 


