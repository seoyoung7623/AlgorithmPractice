/*
재귀함수
2진수로 변환하는 함수
*/
class Solution {
    static int total_remove = 0;
    
    public int binary(String s, int total){
        if (s.equals("1")){
            return total;
        }
        int cnt = 0;
        for (int i=0;i<s.length();i++){
            char c = s.charAt(i);
            if(c == '0'){
                total_remove++;
            } else {
                cnt++;
            }
        }
        String s2 = Integer.toString(cnt,2);
        return binary(s2,total + 1);
    }
    
    public int[] solution(String s) {
        int total = binary(s,0);
        int[] answer = new int[]{total,total_remove};
        return answer;
    }
}