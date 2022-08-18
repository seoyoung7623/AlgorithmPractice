#1003 피보나치
#다이나믹 프로그래밍 동적 프로그래밍을 이용해 시간을 단축한다.

# 재귀함수는 시간이 많이 걸림
# def fibonacci(n):
#     if n==0:
#         fibolist.append('0')
#         return 0 
#     elif n==1:
#         fibolist.append('1')
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
    
# num = int(input())
# for i in range(num):
#     n = int(input())
#     fibolist = []
#     fibonacci(n)
#     print(fibolist.count('0'),fibolist.count('1'),end=' ')
#     print()

#함수를 들어가는 횟수
zero = [1,0,1] 
one = [0,1,1]

def fibonacci(num):
    length = len(zero)
    if num >= length:
        for i in range(length,num+1):
            zero.append(zero[i-1] + zero[i-2])
            one.append(one[i-1] + one[i-2])
    print("{} {}".format(zero[num],one[num]))

t = int(input())
for _ in range(t):
    fibonacci(int(input()))
