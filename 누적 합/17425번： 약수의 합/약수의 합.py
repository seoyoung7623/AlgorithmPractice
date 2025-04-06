#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 17425                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: seoyoung7623 <boj.kr/u/seoyoung7623>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/17425                          #+#        #+#      #+#     #
#    Solved: 2025/04/02 20:35:22 by seoyoung7623  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
'''
N의 크기 1e6 을 1초안에 실행해야하는데 그러면 약수의 합을 바로 저장해야함
'''

# T = int(input())
# memory = [0]

# for i in range(1,1000001):
#     g = 0
#     for j in range(1,i+1):
#         if i % j == 0:
#             g += j
#     memory.append(memory[-1]+g)

# for test_case in range(T):
#     N = int(input())
#     print(memory[N])

'''
약수의 합: 배수에 그 값을 추가한다.
g(x) : 모든 f(x)를 더한값
f(x) : x의 약수의 합

+pypy로 해야 정답인 문제.. 뭐지
'''
import sys
input = sys.stdin.readline
T = int(input())
MAX = 1000000
g = [0] * (MAX + 1)
f = [0] * (MAX + 1)

# 약수의 합: 배수값에 해당값을 더함
for i in range(1, MAX + 1):
    for j in range(i,MAX + 1,i):
        g[j] += i
    f[i] = f[i-1] + g[i]

# # 누적합
# for i in range(1,MAX+1):
#     f[i] = f[i-1] + g[i]

ans = []
for test_case in range(T):
    N = int(input())
    ans.append(N)
for i in ans:
    print(f[i])