# x,y = [1,2]

# print(x)
# print(y)

#2023.01.04
# n = 5
# for i in (n-1,n+1,n*2):
#     print(i)
''' 큐에 리스트 형식으로 추가할 경우
from collections import deque


q = deque([3])
q.append([5])
q.append(4)

print(q)
'''

#2023.01.08 음수 인덱스
'''
listtest = [1,2,3,4,5,6,7,8,9]
print(listtest[-3])
print(listtest[-1])
'''

#2023.01.09
'''
import sys
input = sys.stdin.readline()

num = map(int,input.split())

for i in num:
    print(i)
'''

#2023.01.10
'''
graph = [[1,2,3,4,5,6] for _ in range(5)]
graph[3] += [4] #그래프 3에 4를 추가한다. 하나의 리스트 인덱스에 추가됨
print(graph[3])

graph = []
graph += [4] #리스트 붙이기!
print(graph)

'''

#2023.01.11
# graph = [0 for _ in range(20)]
# for i in graph:
#     print(i)

#2023.07.10
# for i in range(10,0,-1):
#     print(i)

# print(list('tytytyty'))

# a = '123112341231'
# a.replace('1231','X')
# print(a)
# num = a.count('X')
# print(num)
# a = 'hello world'
# a.replace('hello','hi')
# print(a)

## 햄버거 쌓기
# def solution(ingredient):
#     answer = 0
#     hamburger = ''.join(map(str, ingredient))
    
#     while 1:
#         if '1231' in hamburger:
#             answer += hamburger.count('1231')
#             hamburger = hamburger.replace('1231','')
#         else:
#             break
#     return answer
# print(solution([2, 1, 1, 2, 3, 1, 2, 3, 1]))

## 2024.01.04 PGM) 입문자 코테
def solution(n):
    # answer = []
    n_str = list(str(n))
    n_str_reverse = n_str.reverse()
    answer = '[' + ','.join(n_str_reverse)+']'

    return answer
print(solution(12345))