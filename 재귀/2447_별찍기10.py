# G5
'''
리스트 * 곱하기를 이용한다.
첫줄 * -> *** -> ********* n//3씩재귀를 실행
둘째줄 * * -> * *   * * -> 가운데를 비워줘야하기때문에 ' '*(n//3)

반복문과 문자열 * 방식을 적절히 섞어서 주는 재귀 문제
'''

N = int(input())

def draw_star(n):
    if n == 1:
        return ['*']
    prev = draw_star(n//3)
    stars = []

    for row in prev: # 해당 줄 세로로 3줄
        stars.append(row*3) # 각 '*'x3
    for row in prev:
        stars.append(row + ' '*(n//3)+row) # 가운데 빈칸
    for row in prev: # 각 '*'x3
        stars.append(row*3)
    return stars
print('\n'.join(draw_star(N)))