#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 14719                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: seoyoung7623 <boj.kr/u/seoyoung7623>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/14719                          #+#        #+#      #+#     #
#    Solved: 2025/04/03 09:36:35 by seoyoung7623  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
'''
1. 전체 가능 칸의 개수중 빼기
2. 그리디
현재 위치 min(왼쪽 가장 큰높이, 오른쪽 가장 큰높이)- 현재 높이
'''
import sys
input = sys.stdin.readline

H,W = map(int,input().split())
arr = list(map(int,input().split()))

right_height = [0]*W
left_height = [0]*W
left_height[0] = arr[0]
right_height[-1] = arr[-1]

for i in range(1,W):
    left_height[i] = max(left_height[i-1],arr[i])
for i in range(W-2,-1,-1):
    right_height[i] = max(right_height[i+1],arr[i])
    
answer = 0
for i in range(W):
    answer += min(left_height[i],right_height[i])-arr[i]

print(answer)