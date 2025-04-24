#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2745                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: seoyoung7623 <boj.kr/u/seoyoung7623>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2745                           #+#        #+#      #+#     #
#    Solved: 2025/04/22 09:25:57 by seoyoung7623  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
'''
1010=10
문자열인지 숫자인지 확인하는 방법
헐 파이썬 int() 함수가 문자열오 숫자로 바꿔주네 처음 알았음
int(str, base) -> base진수 수를 10진수로 변경해줌
'''
N,M = input().split()
M = int(M)

# total = 0
# length = len(N)
# for i in range(length):
#     n = N[length-i-1]
#     if isinstance(n,str):
#         n = ord(n)-55
#         print(n)
#     total += n ** i
# print(total)

result = int(N,M)
print(result)