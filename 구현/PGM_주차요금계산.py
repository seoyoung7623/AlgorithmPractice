# 주차요금 계산
'''
딕셔너리 deque이용
'''
from collections import deque
import math

def solution(fees, records):
    answer = []
    parking = {}
    for record in records:
        time,number,type_ = record.split()
        if number not in parking:
            parking[number] = deque([time])
        else:
            parking[number].append(time)
    numbers = list(parking.keys())
    numbers.sort()
    for number in numbers:
        price = 0
        total = 0

        while parking[number]:
            in_ = parking[number].popleft()
            in_h,in_m = map(int,in_.split(":"))
            if not parking[number]:
                out_h,out_m = 23,59
            else:
                out_ = parking[number].popleft()
                out_h,out_m = map(int,out_.split(":"))
            if out_m >= in_m:
                total += (out_h-in_h)*60+(out_m - in_m)
            else:
                total += (out_h-in_h-1)*60+(60-in_m)+out_m
                
        if total<=fees[0]:
            price += fees[1]
        else:
            price += fees[1] + math.ceil((total-fees[0])/fees[2])*fees[3]
        answer.append(price)    
    return answer

print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))