# 3752. 가능한 시험 점수 D4

# 조합 문제
# 가 아니라 DP 문제!

T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    scores = list(map(int,input().split()))
    scoreSet = {0}

    for s in scores:
        newSet = set()
        for dp in scoreSet:
            newSet.add(dp+s)
        scoreSet.update(newSet)
    print(f"#{test_case} {len(scoreSet)}")
            