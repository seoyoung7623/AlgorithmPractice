# 조합 라이브러리 없이 구현
def comb(arr,n):
    result = []

    def backtrack(start,comb): # comb 리스트
        if len(comb) == n: # 종료식
            result.append(list(comb))
            return
        for i in range(start,len(arr)):
            comb.append(arr[i])
            backtrack(i+1,comb)
            comb.pop() # 마지막 인덱스를 꺼냄
    
    backtrack(0,[])
    return result
    
print(comb([1,2,3,4],2))