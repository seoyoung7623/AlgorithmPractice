# 2021 카카오 인턴십) 표편집 Lv3 구현
'''
dictionary를 이용한 연결리스트 방법
'''
def solution(n,k,cmd):
    cur = k
    table = {i:[i-1,i+1] for i in range(n)}
    answer = ['O'] * n
    table[0] = [None,1]
    table[n-1] = [n-2,None]
    stack = []

    for c in cmd:
        if c == 'C': # 삭제
            answer[cur] = 'X'
            prev,next = table[cur]
            stack.append([prev,cur,next])
            # 삭제 후 현 위치
            if next == None:
                cur = table[cur][0]
            else:
                cur = table[cur][1]
            # 삭제 후 연결리스트 연결수정
            if prev == None:
                table[next][0] = None
            elif next == None:
                table[prev][1] = None
            else:
                table[prev][1] = next
                table[next][0] = prev

        elif c == 'Z': # 복구
            prev, now, next = stack.pop()
            answer[now] = 'O'
            # 복구된 칸의 연결설정
            if prev == None:
                table[next][0] = now
            elif next == None:
                table[prev][1] = now
            else:
                table[next][0] = now
                table[prev][1] = now
        else:
            # 이동
            c1,c2 = c.split(' ')
            c2 = int(c2)
            if c1 == 'U':
                for _ in range(c2):
                    cur = table[cur][0] # 위로 차례대로 이동
            else:
                for _ in range(c2):
                    cur = table[cur][1] # 아래로 차례대로 이동
    return ''.join(answer)

print(solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))