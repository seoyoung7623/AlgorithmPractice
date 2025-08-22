class Solution {
    public int solution(int n, String control) { 
        for(int i=0;i<control.length();i++){
            char c = control.charAt(i); //i번째 문자열 꺼내기 객체이기때문에
            switch(c){
                case 'w':
                    n += 1;
                    break;
                case 's':
                    n -= 1;
                    break;
                case 'd':
                    n += 10;
                    break;
                case 'a':
                    n -= 10;
                    break;
            }
        }
        int answer = n;
        return answer;
    }
}