# 베스트 앨범 

# 내 코드
def solution(genres, plays):
    answer = []
    genres_list = []
    dic = {}
    
    # 딕셔너리에 장르:[인덱스,횟수] 저장
    for i in range(len(genres)):
        if genres[i] not in dic:
            dic[genres[i]] = [[i,plays[i]]]
        else:
            dic[genres[i]].append([i,plays[i]])

    # 장르별로 총 횟수 구해서 순서 정렬
    for genre in dic:
        dic[genre].sort(key = lambda x:-x[1])
        genre_sum = sum(item[1] for item in dic[genre])
        genres_list.append([genre,genre_sum])
    genres_list.sort(key = lambda x:-x[1])
    
    # 중요!!
    for genre, _ in genres_list:
        for i,p in dic[genre][:2]:
            answer.append(i)
        # answer.append(dic[genre][:2]) #파이썬의 슬라이스는 인덱스가 2보다 작아도 에러가 나지 않음

    return answer

'''
딕셔너리2개를 이용해 깔끔하게 정리가능
'''
def solution1(genres, plays):
    answer = []
    dic1 = {}
    dic2 = {}

    for i,(g,p) in enumerate(zip(genres,plays)):
        # 음원 각각의 횟수
        if g not in dic1:
            dic1[g] = [(i,p)]
        else:
            dic1[g].append((i,p))
        
        # 장르별 총음원 횟수
        if g not in dic2:
            dic2[g] = p
        else:
            dic2[g] += p
    
    for k,v in sorted(dic2.items(),key= lambda x:x[1],reverse=True):
        for (i,p) in sorted(dic1[k],key= lambda x: x[1],reverse=True)[:2]:
            answer.append(i)
    return answer
print(solution(["classic", "pop", "classic", "classic", "pop"],[500, 600, 150, 800, 2500]))