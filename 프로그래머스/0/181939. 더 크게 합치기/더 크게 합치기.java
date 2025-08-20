class Solution {
        public int solution(int a, int b) {
        int answer = 0;
        String s1 = Integer.toString(a) + Integer.toString(b);
        String s2 = Integer.toString(b) + Integer.toString(a);
        int answer1 = Integer.parseInt(s1);
        int answer2 = Integer.parseInt(s2);
        if (answer2 > answer1) {
            return answer2;
        } else {
            return answer1;
        }
    }
}