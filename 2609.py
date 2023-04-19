#2609 최대공약수와 최소공배수
import sys
input =  sys.stdin.readline

n1,n2 = map(int,input().split())
def gcd(n1,n2):
    while n2>0:
        n1,n2 = n2, n1%n2
    return n1

def lcm(n1,n2):
    return (n1*n2)//gcd(n1,n2)

print(gcd(n1,n2))
print(lcm(n1,n2))





# import sys
# input =  sys.stdin.readline

# n1,n2 = map(int,input().split())
# myMin = 0
# myMax = 0
# for i in range(1,min(n1,n2)+1):
#     if n1%i==0 and n2%i==0:
#         myMin = i
# myMax = max(n1,n2)
# while 1:
#     myMax +=1
#     if myMax%n1 == 0 and myMax%n2 ==0:
#         break
# print(myMin)
# print(myMax)