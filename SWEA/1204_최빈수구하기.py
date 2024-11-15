# 최빈수 구하기 D2
'''
1. 딕셔너리에 값저장하기
2. 리스트의 인덱스를 점수로 설정
'''
from 브루트포스.PGM_피로도 import answer

# 딕셔너리에 값 저장하기
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    numList = list(map(int, input().split()))
    answer = []
    dic = {}
    for i in range(len(numList)):
        if numList[i] not in dic:
            dic[numList[i]] = 1
        else:
            dic[numList[i]] += 1
    max_value = max(dic.values())
    for k,v in dic.items():
        if v == max_value:
            answer.append(k)
    answer = sorted(answer, reverse=True)
    print(f'#{N} {answer[0]}')

# 리스트의 인덱스를 점수라고 설정
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    numList = list(map(int, input().split()))
    score = [0]*1001
    answer = []
    for i in range(len(numList)):
        score[numList[i]] += 1
    max_count = max(score)
    for i in range(len(numList)):
        if score[numList[i]] == max_count:
            answer.append(numList[i])
    answer.sort(reverse=True)
    print(f'#{N} {answer[0]}')


