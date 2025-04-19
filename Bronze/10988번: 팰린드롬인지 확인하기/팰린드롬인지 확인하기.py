#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 10988                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: seoyoung7623 <boj.kr/u/seoyoung7623>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/10988                          #+#        #+#      #+#     #
#    Solved: 2025/04/18 09:48:06 by seoyoung7623  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
answer = input()
for i in range(len(answer)//2):
    if answer[i] != answer[len(answer)-i-1]:
        print(0)
        break
else:
    print(1)