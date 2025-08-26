import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static int knapsack(int[][] values, int k){
        int[] dp = new int[k+1];
        for (int[] item:values){
            int w = item[0]; int v = item[1];
            for (int i=k;i>=w;i--) {
                dp[i] = Math.max(v + dp[i - w], dp[i]);
            }
        }
        int answer = dp[k];
        return answer;
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine()); // 공백단위로 문자열을 끊어줌
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        int [] W = new int[N+1];
        int [] V = new int[N+1];
        int [][] values = new int[N+1][2];

        for (int i=1;i<=N;i++){
            st = new StringTokenizer(br.readLine());
            values[i][0] = Integer.parseInt(st.nextToken());
            values[i][1] = Integer.parseInt(st.nextToken());
        }
        System.out.println(knapsack(values,K));
    }
}
