# SW마에스트로 16기 1차 3번
from itertools import combinations

def brute_force_possible_numbers(n, k, questions):
    # 1부터 n까지 중에서 k개를 선택하는 모든 조합 생성
    all_combinations = list(combinations(range(1, n + 1), k))
    
    # 조건을 만족하는 조합만 필터링
    valid_combinations = []
    
    for comb in all_combinations:
        valid = True
        for x, y in questions:
            count = sum(1 for num in comb if num >= x)  # x 이상인 숫자의 개수 확인
            if count != y:
                valid = False
                break
        if valid:
            valid_combinations.append(comb)
    
    # 각 자리에서 가능한 숫자의 개수 계산
    possible_counts = [set() for _ in range(k)]
    for comb in valid_combinations:
        for i, num in enumerate(comb):
            possible_counts[i].add(num)

    return [len(possible_counts[i]) for i in range(k)]

# 테스트 실행 (완전 탐색으로 검증)
n, k, questions = 15, 3, [[7,1],[15,0],[14,1],[3,3],[5,2]]
brute_force_result = brute_force_possible_numbers(n, k, questions)

# 결과 확인
print(brute_force_result)