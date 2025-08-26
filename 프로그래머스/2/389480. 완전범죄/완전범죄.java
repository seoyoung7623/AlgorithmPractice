/*
A도둑이 더 최솟값이 경우로
B도둑은 최대로
백트래킹? 조합과 비슷?

왜 DP지..
1. 최적부분구조: 현재 물건까지의 최적해는, 이전 물건들까지의 최적해에서만 파생됨.
2. 중복부분문제
값들을 다 저장하면 메모리를 많이 쓸것 같은데..
값들중에 가능하면서도 A가 작은걸로 변환 이게 DP의 핵심인듯
*/
/*
1차원 DP방식 풀이
dp, next로 문제풀이 next는 매번 inf로 초기화
*/
import java.util.*;

class Solution {
    static final int INF = 1_000_000_000;
    
    public int solution(int[][] info, int n, int m) {
        int answer = INF;
        int[] dp = new int[m];
        Arrays.fill(dp,INF);
        dp[0] = 0;
            
        for (int[] item:info){
            int a = item[0]; int b = item[1];
            int[] next = new int[m];
            Arrays.fill(next,INF);
            
            for (int j=0;j<m;j++){
                if (dp[j]==INF) continue;
                
                // A에게 주는 경우
                next[j] = Math.min(next[j],dp[j]+a);
                
                // B에게 주는 경우
                if (j+b<m){
                    next[j+b] = Math.min(next[j+b],dp[j]);
                }                
            }
            dp = next;
        }
        for (int i=0;i<m;i++){
            answer = Math.min(answer,dp[i]);
        }
        return (answer < n)?answer:-1;
    }
}