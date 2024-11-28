# 여행경로 Lv3
def solution(tickets):
    answer = []
    visited = [False] * len(tickets)
    
    def DFS(port,lst):
        if len(list(lst)) == len(tickets)+ 1:
            answer.append(list(lst))
            return
        for i,ticket in enumerate(tickets):
            if ticket[0] == port and not visited[i]:
                visited[i] = True
                DFS(ticket[1],lst + [ticket[1]])
                visited[i] = False

    DFS("ICN",["ICN"])      
    answer = sorted(answer)[0]  
    return answer

print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))