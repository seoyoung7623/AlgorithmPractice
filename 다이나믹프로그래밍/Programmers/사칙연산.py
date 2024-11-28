# 사칙연산
'''
최대구하기 : 1.(최대) + (최대) 2.(최대) - (최소)
최소구하기 : 1.(최소) + (최소) 2.(최소) - (최대)
'''
def solution(arr):
    arrs = ''.join(arr).split('-')
    val0 = sum(list(map(int, arrs[0].split('+'))))  #첫수는 무조건 합이 될수밖에 없음
    if len(arrs) == 1:
        return val0
    min_val = 0
    max_val = 0
    
    for arr in arrs[:0:-1]: #뒤에서 부터
        x = list(map(int, arr.split('+')))
        _min_val = -(sum(x)) # -(8+3)
        _max_val = sum(x[1:]) - x[0] # 최대값은 첫수에서 음수를 적용한 경우 (-8)+3
        min_val, max_val = min(_min_val + min_val, _min_val - max_val), max(_max_val + max_val, _min_val - min_val)

    return val0 + max_val # 첫번째 값 + 최댓값
print(solution(["1", "-", "3", "+", "5", "-", "8"]))