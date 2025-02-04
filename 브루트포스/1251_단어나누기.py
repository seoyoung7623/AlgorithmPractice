# 단어나누기 S5
'''
제한 용량과 시간이 충분해서 브루투포스로 풀 수 있다.
'''
# word = input()

# first = word.index(min(word[:-2]))
# sec = word.index(min(word[first+1:-1]))
# third = word.index(min(word[sec+1:]))

# word = list(word)

# answer = ''.join(reversed(word[:first+1]))
# answer += ''.join(reversed(word[first:sec]))
# answer += ''.join(reversed(word[sec:third]))

# print(answer)
'''
이 코드가 틀린 이유는?
최소 문자의 위치만 보고 나누면, 가장 작은 사전순 단어가 아닐 가능성이 큼.
모든 나누는 방법을 탐색해서 가장 작은 사전순 단어를 선택해야 함!
'''

word = input()
words = []

for i in range(1,len(word)):
    for j in range(i+1,len(word)):
        answer = ''.join(reversed(word[:i]))
        answer += ''.join(reversed(word[i:j]))
        answer += ''.join(reversed(word[j:]))
        words.append(answer)

print(sorted(words)[0])
