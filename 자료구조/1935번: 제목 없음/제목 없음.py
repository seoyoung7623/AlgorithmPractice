#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1935                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: seoyoung7623 <boj.kr/u/seoyoung7623>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1935                           #+#        #+#      #+#     #
#    Solved: 2025/06/05 09:31:59 by seoyoung7623  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
'''
후위 표기식
123*+45/-
(1+(2*3))-(4/5) = 
7-0.8 = 

후위표기식 알고리즘
스택
'''
N = int(input())
line = input()
dic = {}
for i in range(N):
    dic[chr(i+65)] = int(input())
stack = []

for i in line:
    if i =='+':
        a,b = stack.pop(),stack.pop()
        stack.append(a+b)
    elif i =='*':
        a,b = stack.pop(),stack.pop()
        stack.append(a*b)
    elif i =='-':
        a,b = stack.pop(),stack.pop() # a,b 순서 주의
        stack.append(b-a)
    elif i =='/':
        a,b = stack.pop(),stack.pop()
        stack.append(b/a)
    else:
        stack.append(dic[i])
print(f"{stack[0]:.2f}")
