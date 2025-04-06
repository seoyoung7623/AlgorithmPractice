#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 13908                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: seoyoung7623 <boj.kr/u/seoyoung7623>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/13908                          #+#        #+#      #+#     #
#    Solved: 2025/04/06 22:31:41 by seoyoung7623  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
'''
1. 수학계산
2. 백트래킹 어떻게 하지 전체 경우를 다 봐야할것 같은데 그럼 arr 값이 모두 들어있는지도 확인해야해
조합을 활용한 문제
issubset() 함수: A가 B집합안에 다 포함되어있으면 True
'''
n,m = map(int,input().split())
if m != 0: 
    arr = set(map(int,input().split()))
else: #0인경우 입력을 받지 않음
    arr = set()
answer = 0

def backtracking(length,used_digits):
    global answer
    if length == n:
        if arr.issubset(used_digits):
            answer += 1
        return
    for i in range(10):
        new_digits = used_digits.copy() # 새로 갱신 이렇게하면 set집할이라도 모든 수를 추가할수있음
        new_digits.add(i)
        backtracking(length+1,new_digits)

backtracking(0,set())
print(answer)


