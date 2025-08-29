/*
비스마스크로 전체 탐색
*/
import java.util.*;

class Solution {
    public int solution(int n, int[][] q, int[] ans) {
        int m = q.length;
        
        long[] masks = new long[m];
        for (int i=0;i<m;i++){
            long mask = 0L;
            for (int x:q[i]){
                mask |= (1L << (x-1));
            }
            masks[i] = mask;
        }
        int count = 0;
        
        for (int a=1;a<=n-4;a++){
            for (int b=a+1;b<=n-3;b++){
                for (int c=b+1;c<=n-2;c++){
                    for (int d=c+1;d<=n-1;d++){
                        for (int e=d+1;e<=n;e++){
                            long cond = (1L << (a-1)) | (1L << (b-1)) | (1L << (c-1)) | (1L << (d-1)) | (1L << (e-1));
                            if (isValid(cond,masks,ans)){
                                count++;
                            }
                        }
                    }
                }
            }
        }
        return count;
    }
    
    private boolean isValid(long cond, long[] masks, int[] ans){
        for (int i = 0; i<masks.length; i++){
            int inter = Long.bitCount(cond & masks[i]);
            if (inter != ans[i]) return false;
        }
        return true;
    }
}