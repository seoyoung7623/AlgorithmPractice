# 2869 달팽이는 올라가고 싶다. B1
import math
A,B,C = map(int,input().split())
day = math.ceil((C-A)/(A-B))+1
print(day)

