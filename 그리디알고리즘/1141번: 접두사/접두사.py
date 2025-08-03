#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1141                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: seoyoung7623 <boj.kr/u/seoyoung7623>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1141                           #+#        #+#      #+#     #
#    Solved: 2025/04/29 09:32:39 by seoyoung7623  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
'''
접두사가 다른 최대 개수

⭐️ 내림차순으로 정렬(이거 생각하기)
입렵된 단어들 중복된 단어가 있을 수 있음 제거하기
접두사가 나오면 넘어감, 접두사가 아니면 추가

startswith() 함수 사용
'''
import sys
input = sys.stdin.readline

N = int(input())
lst = [input().rstrip() for _ in range(N)]
lst.sort(key=lambda x:-len(x))
answer = []

for i in range(len(lst)):
    for j in range(len(answer)):
        if answer[j].startswith(lst[i]):
            break
    else:
        answer.append(lst[i])

print(len(answer))
