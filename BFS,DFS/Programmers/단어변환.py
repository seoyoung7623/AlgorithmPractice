# 단어변환
from collections import deque
def solution(begin, target, words):
    answer = 0
    if target not in words:
        return 0
    else:
        q = deque([[begin,0]])
        while q:
            now,depth = q.popleft()
            if now == target:
                return depth     
            for word in words:
                cnt = 0
                for i in range(len(now)):
                    if word[i] != now[i]:
                        cnt += 1
                if cnt == 1: # 다른 알파벳이 하나라면?
                    q.append([word,depth+1])
                    words.remove(word)
print(solution("hit","cog",["hot", "dot", "dog", "lot", "log", "cog"]))