# 2800 괄호 제거 G4
'''
접근 방법은 맞음
괄호의 쌍을 저장하고 모든 조합을 구해서 제거한다.
여기서 제거는 del을 이용할 수 있지만 리스트를 문자열로 변환하는 과정에서 ''.join을 이용하므로
한번에 여러 인덱스 값을 제거하고 싶을떼 인덱스 값을 ''로 변경해주면 된다!

정답 answer 에 중복제거를 해야하는 이유?
(1+(2*3)+((8)/4))+1
[(1,12), (5,7)] → "1+(2*3)+(8/4)+1"
[(5,7), (1,12)] → "1+(2*3)+(8/4)+1"
조합이 중복되어 생성되는 경우 발생
'''
from itertools import combinations

arr = list(input())
stack = []
twin = []
answer = set()
for i in range(len(arr)):
    if arr[i] == '(':
        stack.append(i)
    elif arr[i] == ')':
        twin.append((stack.pop(),i))

for i in range(len(twin)):
    for combo in combinations(twin,i+1):
        arr_copy = arr[:] #깊은 복사가 필요없는 이유는?
        for idx in combo:
            arr_copy[idx[0]] = arr_copy[idx[1]] = ''
        answer.add(''.join(arr_copy))

for string in sorted(list(answer)):
    print(string)

'''
깊은복사 vs 얕은복사
깊은복사:copy.deepcopy(리스트), 2차원 리스트와 같이 내부 저장공간을 공유하는 경우 깊은 복사를 해야함
얕은복사: copy.copy(리스트), 리스트[:]
'''