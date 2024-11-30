# 18130 여름나기 B1
'''
등차수열의 합
'''
import math 
N,Q = map(int,input().split())  
arr = []
for n in range(1,N+1):
    P,K,C = map(int,input().split())
    pay = 0
    T = Q//K
    pay = C*(T*(T-1)//2) + P
    if Q%K != 0:
        pay += T*C
    arr.append((n,pay))  
min_pay = min(arr,key=lambda x:(x[1],x[0]))
print(min_pay[0],min_pay[1])
