# 9251 lcs
import sys
input = sys.stdin.readline

# 2차원 배열 방식
word1,word2 = input().strip(), input().strip()
l1,l2 = len(word1),len(word2)
cache = [[0] * (l2+1) for _ in range(l1+1)]

for i in range(1,l1+1):
    for j in range(1,l2+1):
        if word1[i-1] == word2[j-1]:
            cache[i][j] = cache[i-1][j-1] + 1
        else:
            cache[i][j] = max(cache[i][j-1],cache[i-1][j])
print(cache[-1][-1])

# 1차원 배열 방식 (캐시)
word1,word2 = input().strip(), input().strip()
l1,l2 = len(word1),len(word2)
cache = [0] * l2
for i in range(l1):
    cnt = 0
    for j in range(l2):
        if cnt < cache[j]: # word가 같음을 확인하기 이전에 누적값이 있는지 확인한다. 누적값이 있으면 cnt 갱신
            cnt = cache[j]
        elif word1[i] == word2[j]: #elif로 처리하여 현재 누적값이후 값을 처리해줌
            cache[j] = cnt + 1
print(max(cache))

    