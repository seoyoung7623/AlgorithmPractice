'''
투포인터로
한번 움직임을 저장하는 방식 removed 저장 중요
'''
import sys
input = sys.stdin.readline

T = int(input())

def palindrome(word,right,left,removed):
    while right < left:
        if word[right] != word[left]:
            if removed:
                return False
            return palindrome(word, right+1,left, True) or palindrome(word, right, left-1,True)
        right += 1
        left -= 1
    return True

def check_palindrome(word):
    if palindrome(word,0,len(word)-1,True):
        return 0
    elif palindrome(word,0,len(word)-1,False):
        return 1
    else:
        return 2
                
for _ in range(T):
    word = input().rstrip()
    answer = check_palindrome(word)
    print(answer)
