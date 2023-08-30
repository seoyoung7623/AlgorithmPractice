# 길찾기 게임
import sys
sys.setrecursionlimit(10**6) # 재귀 호출을 더 깊게 해줌

def preOrder(arrY,arrX,answer): # 전위순회
    node = arrY[0] # 가장 위에 있는 노드
    idx = arrX.index(node) #가장 위에 있는 노트의 인덱스
    arrY1 = []
    arrY2 = []

    for i in range(1,len(arrY)):
        if node[0] > arrY[i][0]: # x값이 작은 값을 찾음
            arrY1.append(arrY[i])
        else:
            arrY2.append(arrY[i]) # x가 오른쪽에 있을때
    answer.append(node[2]) # 노드의 인덱스를 먼저 넣음 step1
    if len(arrY1) > 0 : # 작은 값 노드가 있는 경우 step2
        preOrder(arrY1,arrX[:idx],answer)
    if len(arrY2) > 0: # 오른쪽 재귀 step3
        preOrder(arrY2,arrX[idx+1:],answer)
    return

def postOrder(arrY,arrX,answer):
    node = arrY[0]
    idx = arrX.index(node)
    arrY1 = []
    arrY2 = []

    for i in range(1,len(arrY)):
        if node[0] > arrY[i][0]:
            arrY1.append(arrY[i])
        else:
            arrY2.append(arrY[i])
    if len(arrY1) > 0: # step1
        postOrder(arrY1,arrX[:idx],answer)
    if len(arrY2) > 0 : # step2
        postOrder(arrY2,arrX[idx+1:],answer)
    answer.append(node[2]) # 후위순회이므로 재귀를 다 한후에 노드를 넣음 step3
    return

def solution(nodeinfo):
    preAnswer = []
    postAnswer = []

    for i in range(len(nodeinfo)):
        nodeinfo[i].append(i+1)
    arrY = sorted(nodeinfo,key = lambda x:(-x[1],x[0])) # 트리 순서대로 정렬
    arrX = sorted(nodeinfo) # 정렬

    preOrder(arrY,arrX,preAnswer)
    postOrder(arrY,arrX,postAnswer)

    return [preAnswer,postAnswer]
print(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]))