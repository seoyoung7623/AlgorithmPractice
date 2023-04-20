'''
지능형 리스트

(변수를 활용해 만들 값) for (변수 명) in (순회할 수 있는 값)

listComprehension으로 된 코드를 읽을 때는 for뒤에서 부터 읽으면 편하다.

'''

## 백준 온라인 저지 1920번 "수 찾기" (http://boj.kr/1920)
import sys
input = sys.stdin.readline

_ = input()
_set = set(map(int, input().split()))
q = input()
_list = list(map(int, input().split()))

print(*[1 if dt in _set else 0 for dt in _list], sep = '\n')

'''
이 코드에서
_list 안을 순환할때 dt인 경우 dt가 _set안에 있으면 1을 반환한다

'''