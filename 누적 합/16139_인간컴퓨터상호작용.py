# 16139 인간-컴퓨터 상호작용 S1
'''
실시간 전처리보다 완전 전처리를 해야 정답임
아.. pypy3로 하니까 됨..;;
'''
import sys
input = sys.stdin.readline
S = input()
q = int(input())

alphabet_dic = {}

for alphabet in range(ord('a'),ord('z')+1):
    s_arr = [0]*(len(S)+1)
    for idx in range(1,len(S)+1):
        if ord(S[idx-1]) == alphabet:
            s_arr[idx] += 1
        s_arr[idx] += s_arr[idx-1]
    alphabet_dic[chr(alphabet)] = s_arr

for _ in range(q):
    a,l,r = input().rstrip().split()
    l,r = int(l),int(r)

    s_arr = alphabet_dic[a]
    
    print(s_arr[r+1] - s_arr[l])
