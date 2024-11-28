# 숫자타자 대회
'''
- DP
왼손과 오른손의 위치를 저장하고, 현재 위치에서 다음 위치로 이동하는데 드는 비용을 계산하여
왼손과 오른손의 위치를 갱신하며 최소 비용을 계산한다.
'''
def solution(numbers):
    key_pad = {
        '1': (0, 0), '2': (0, 1), '3': (0, 2),
        '4': (1, 0), '5': (1, 1), '6': (1, 2),
        '7': (2, 0), '8': (2, 1), '9': (2, 2),
        '0': (3, 1)
    }

    def cost(pos1, pos2):
        if pos1 == pos2:
            return 1
        x1,y1 = pos1
        x2,y2 = pos2
        dx,dy = abs(x1-x2),abs(y1-y2)
        if dx+dy == 1:
            return 2
        elif dx == 1 and dy == 1:
            return 3
        else:
            return 2*(dx+dy)-min(dx,dy)

    l_pos = key_pad['4']
    r_pos = key_pad['6']
    dp = {(l_pos, r_pos): 0}

    for number in numbers:
        new_dp = {}
        next_pos = key_pad[number]
        for (l_pos, r_pos), current in dp.items():
            if l_pos != next_pos: # 왼손에 있을경우 그 수를 누름
                left_cost = current + cost(l_pos, next_pos)
                new_dp[(next_pos, r_pos)] = min(new_dp.get((next_pos, r_pos), float('inf')), left_cost)
            
            if r_pos != next_pos:
                right_cost = current + cost(r_pos, next_pos)
                new_dp[(l_pos, next_pos)] = min(new_dp.get((l_pos, next_pos), float('inf')), right_cost)
        dp = new_dp
    
    return min(dp.values())

        
print(solution("5123"))
print(solution("1756"))