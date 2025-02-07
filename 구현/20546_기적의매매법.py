# 20546 기적의 매매법 S5
'''
이 문제를 해석하는데만 1시간이 걸림
role로 3번을 계산하지 말고 인덱스로 3이전을 판단하면 된다..
파이썬은 여러개 크기 비교를 쉽게 할 수 있기 때문!
'''

total = int(input())
stocks = list(map(int,input().split()))

jun_total, sung_total = total, total
jun_stock, sung_stock = 0,0

# BNP
for i in range(14):
    jun_stock += (jun_total // stocks[i])
    jun_total %= stocks[i]

# TIMING
role = 0
for i in range(3,14):
    # 상승장
    if stocks[i-3] < stocks[i-2] < stocks[i-1] < stocks[i]:
        sung_total += stocks[i] * sung_stock
        sung_stock = 0
    elif stocks[i-3] > stocks[i-2] > stocks[i-1] > stocks[i]:
        if sung_total > stocks[i]:
            sung_stock += (sung_total // stocks[i])
            sung_total %= stocks[i]

jun_price = jun_total + stocks[-1] * jun_stock
sung_price = sung_total + stocks[-1] * sung_stock
if jun_price > sung_price:
    print("BNP")
elif jun_price < sung_price:
    print("TIMING")
else:
    print("SAMESAME")


