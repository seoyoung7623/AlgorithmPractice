class Solution {
    public int[] solution(int start_num, int end_num) {
        int max_length = start_num-end_num;
        int[] answer = new int[max_length+1];
        for (int i=0;i<=max_length+1;i++){
            if (start_num < end_num){
                break;
            }
            answer[i] = start_num;
            start_num -= 1;
        }
        return answer;
    }
}