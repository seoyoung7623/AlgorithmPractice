import java.util.*;

class Solution {
    public int[] solution(int n) {
        List<Integer> list = new ArrayList<Integer>();
        
        while (true){
            list.add(n);
            if (n == 1){
                break;
            } else if (n%2==0) { //짝
                n /= 2;
            } else{
                n = 3*n+1;
            }
        }
        int[] answer = list.stream().mapToInt(Integer::intValue).toArray();
        return answer;
    }
}