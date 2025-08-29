from itertools import combinations

def solution(n, q, ans):
    answer = 0
    m = len(q)
    q_sets = [set(arr) for arr in q]
    
    count = 0
    
    for cand in combinations(range(1,n+1),5):
        cand_set = set(cand)
        
        ok = True
        for i in range(m):
            if len(cand_set & q_sets[i]) != ans[i]:
                ok = False
                break
        if ok:
            count += 1
        
    
    return count