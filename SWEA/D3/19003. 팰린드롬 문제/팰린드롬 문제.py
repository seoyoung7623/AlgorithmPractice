from collections import Counter

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = map(int,input().split())
    words = [input().strip() for _ in range(N)]
    count = Counter(words)
    
    pairs = 0
    center = 0
    
    for w in words:
        if count[w] == 0:
            continue
        if w[::-1] == w and w[::-1] in words and count[w] == 1:
            if center == 0:
                center += len(w)
                count[w] -= 1
        elif w[::-1] in words:
            count[w] -= 1
            count[w[::-1]] -= 1
            pairs += 2*(len(w))
        #print(center, pairs)
    print(f"#{test_case} {center+pairs}")
        
        
    