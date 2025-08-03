#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 19532                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: seoyoung7623 <boj.kr/u/seoyoung7623>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/19532                          #+#        #+#      #+#     #
#    Solved: 2025/05/07 09:35:47 by seoyoung7623  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
'''
최대 공약수 a,d

크래머의 공식
연립방정식 행렬
ax + by = c  
dx + ey = f
'''
# a,b,c,d,e,f = map(int,input().split())
# a_2,b_2,c_2 = a,b,c
# a *= d
# b *= d
# c *= d

# d *= a_2
# e *= a_2
# f *= a_2

# if (a+d) != 0:
#     y = int((c-f)/(b-e))
# else:
#     y = int((c+f)/(b+e))
# x = (c-b*y)//a
# print(x,y)

a, b, c, d, e, f = map(int, input().split())

denominator = a * e - b * d  # 분모

x = (c * e - b * f) // denominator
y = (a * f - c * d) // denominator

print(x, y)
