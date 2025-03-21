# G5
'''
펠린드롬
회문, 유사회문, 일반문자
유사회문: 한문자를 삭제했을때 회문이 되는지 한문자를 지워서 다시 판단

✅ 투포인터
앞뒤에서 다른 문자가 나왔을때만 체크
'''
# import sys
# input = sys.stdin.readline

# T = int(input())

# def sim_palindrome(str,length):
#     for s in range(length):
#         copy_str = list(str[::])
#         del copy_str[s]
#         if palindrome(copy_str,length-1):
#             return True
#     return False

# def palindrome(str,length):
#     for s in range(0,length//2):
#         if str[s] != str[length-s-1]:
#             return False
#     return True

# for i in range(T):
#     str = input().rstrip()
#     length = len(str)
#     if not palindrome(str,length):
#         if sim_palindrome(str,length):
#             print(1)
#         else:
#             print(2)
#     else:
#         print(0)

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

    