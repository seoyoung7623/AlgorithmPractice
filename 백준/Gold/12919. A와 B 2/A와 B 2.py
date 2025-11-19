import sys
input = sys.stdin.readline

S = input().strip()
T = input().strip()

def dfs(cur):
    # 길이가 같아졌으면 S랑 같은지 체크
    if len(cur) == len(S):
        return cur == S

    res = False

    # 1) 뒤에 A를 추가했었다면 → 지금 문자열의 뒤는 A여야 함
    if cur[-1] == 'A':
        if dfs(cur[:-1]):
            return True  # 하나라도 성공하면 바로 True 리턴

    # 2) 뒤에 B를 붙이고 뒤집었었다면
    #    현재 문자열의 앞이 B일 것
    if cur[0] == 'B':
        nxt = cur[1:][::-1]
        if dfs(nxt):
            return True

    return False  # 아무 방법도 안 통하면 False

if dfs(T):
    print(1)
else:
    print(0)
