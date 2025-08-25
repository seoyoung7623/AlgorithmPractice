/*
스택문제
*/
import java.util.*;

class Solution
{
    public int solution(String s)
    {
        int answer = -1;
        Stack<Character> stack = new Stack<>();
        char c = s.charAt(0);
        stack.push(c);   
        for (int i=1;i<s.length();i++){
            c = s.charAt(i);
            
            if (stack.isEmpty()){
                stack.push(c);
            } else {
                char p = stack.peek(); 
                if (p == c){
                stack.pop();
                } else{
                    stack.push(c);
                }
            }
            
        }
        if (stack.isEmpty()){
            answer = 1;
        } else {
            answer = 0;
        }
        
        System.out.println(answer);

        return answer;
    }
}