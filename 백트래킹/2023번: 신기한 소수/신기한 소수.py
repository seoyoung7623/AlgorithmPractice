#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2023                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: seoyoung7623 <boj.kr/u/seoyoung7623>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2023                           #+#        #+#      #+#     #
#    Solved: 2025/04/24 09:38:02 by seoyoung7623  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
'''
N자리 신기한 소수모두 출력
백트래킹

소수구하는 법 1을 제외한 약수가 1과 본인 자신만 있는 수
0이 들어간 숫자중에 소수가 있나? 있을수도

소수 검사 범위 제곱근으로 하니까 시간 초과안남
'''

N = int(input())
answer = []

def decimal(n):
    if n == 1 or n == 0:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    else:
        return True

def backtracking(lst):
    # 종료 조건 (길이가 4글자인경우 종료)
    if lst:
        number = int(''.join(map(str,lst)))
        if not decimal(number):
            return
        if len(lst) == N:
            answer.append(number)
            return
    # 함수 조건
    for i in range(10):
        lst.append(i)
        backtracking(lst)
        lst.pop()


backtracking([])
for a in answer:
    print(a)