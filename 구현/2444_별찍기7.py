# 2444 별찍기 7 B3
'''
등차 일반항: a+(n-1)d
'''
n = int(input())
for i in range(1,n+1):
    print(' '*(n-i)+'*'*(1+(i-1)*2))
for i in range(n-1,0,-1):
    print(' '*(n-i)+'*'*(1+(i-1)*2))

