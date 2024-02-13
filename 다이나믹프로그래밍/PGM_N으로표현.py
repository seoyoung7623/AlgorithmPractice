# N으로 표현 
'''
n=1:5
n=2:5+5,5-5,5*5,5/5
n=3: n1 (사칙연산) n2, n2 (사칙연산) n1
'''
def solution(N, number):
    answer = 0
    set_list = []
    for cnt in range(1,9):
        partial_set = set() # n개의 사칙연산 값 저장
        partial_set.add(int(str(N) * cnt)) # 이어 붙이는 수
        # 사칙연산의 순서에따라 값이 달리지기 때문에
        for i in range(cnt - 1): #(1,n-1) (n-1,1)까지 사칙연산 
            for op1 in set_list[i]:
                for op2 in set_list[-i-1]:
                    partial_set.add(op1 + op2)
                    partial_set.add(op1 * op2)
                    partial_set.add(op1 - op2)
                    if op2 != 0:
                        partial_set.add(op1/op2)
        if number in partial_set:
            return cnt
        set_list.append(partial_set) # 총 값 n별로 저장
    return -1
print(solution(5,12))