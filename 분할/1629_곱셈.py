# 곱셈 # 거듭제곱 알고리즘 # S1
A, B, C = map(int,input().split())
def pow(a,b):
    if b == 0:
        return 1
    if b % 2 == 0:
        n = pow(a,b//2)
        return n*n%C
    elif b % 2 == 1:
        n = pow(a,b//2)
        return a*n*n%C
print(pow(A,B))