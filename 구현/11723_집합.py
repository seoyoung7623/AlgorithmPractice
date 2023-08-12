# 11723 집합 S5
import sys
input = sys.stdin.readline

M = int(input())
setting = set()

for i in range(M):
    ans = input().strip().split()    # strip() \n값을 지워주는 역할
    if len(ans) == 1:
        ans0 = ans[0]
        if ans0 == "all":
            setting = set(i for i in range(1,21))
            continue
        elif ans0 == "empty":
            setting = set()
            continue
    else:
        ans0,ans1 = ans
        num = int(ans1)
    
        if ans0 == "add":
            setting.add(num)
        elif ans0 == "remove":
            setting.discard(num)
            # 집합의 제거 방법에는 remove,discard,pop이 있다 discard는 원소가 집합에 없는 경우 에러를 띄우지 않고, remove는 에러를 띄운다.
            # pop은 임의의 원소를 제거한다.
            # remove로 하니까 계속 keyError났음...ㅠㅠㅠ
        elif ans0 == "check":
            print(1 if num in setting else 0)
        elif ans0 == "toggle":
            if num in setting:
                setting.discard(num)
            else:
                setting.add(num)
        
