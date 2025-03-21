# 1번 문제
from bisect import bisect_left
from bisect import bisect_right
from collections import defaultdict

def min_moves_to_target(original, target, start):
    n = len(original)
    start -= 1
    pos = start
    moves = 0

    char_positions = defaultdict(list)
    # 각문자의 등장 위치를 사전에 저장
    for i, char in enumerate(original):
        char_positions[char].append(i)
    
    for i,char in enumerate(target):
        if char not in char_positions:
            return -1
        
        indices = char_positions[char]
        right_index = bisect_left(indices,pos)
        