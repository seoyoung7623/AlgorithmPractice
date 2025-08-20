import java.util.Arrays;

class Solution {
    public int[] solution(int[] num_list, int n) {
        int[] lst1 = Arrays.copyOfRange(num_list,0,n);
        int[] lst2 = Arrays.copyOfRange(num_list,n,num_list.length);
        int[] answer = new int[lst1.length + lst2.length];

        System.arraycopy(lst2,0,answer,0,lst2.length); //원본배열, 시작배열, 대응배열, 대응배열 위치
        System.arraycopy(lst1,0,answer,lst2.length,lst1.length);
        return answer;
    }
}