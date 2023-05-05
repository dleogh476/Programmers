//1. 명령어의 좌표와 현재 위치 값을 더한 값이 y값과 x값이 절댓값5를 넘는지 확인
//2. 현재위치에서 명령어 좌표를 더한 값을 현재 위치 값에 저장
//3. 현재값을 지나간 좌표를 저장하는 hashMap에 저장
//방문 hashMap의 Key는 5*y + x 입니다. val는 bool입니다.
//좌표평면을 넘거나 방문한 길은 다시 안감  
import java.util.*;

class Solution {
    int getVal(int x, int y){
        return x*11 + y;
    }
    public int solution(String dirs) {
        int answer = 0;
        int[] point = {5,5};
        char[] dir = dirs.toCharArray();
        boolean[][] vit = new boolean[121][121];
        int val1, val2;
        for(char d : dir){
            switch(d){
                case 'U':
                    if(point[0]+1 <= 10){
                        val1 = getVal(point[0], point[1]);
                        val2 = getVal(point[0]+1, point[1]);
                        point[0] += 1;
                        if(vit[val1][val2]) break;
                        vit[val1][val2] = true;
                        vit[val2][val1] = true;
                        answer++;
                    }
                    break;
                case 'D':
                    if(point[0]-1 >= 0){
                        val1 = getVal(point[0], point[1]);
                        val2 = getVal(point[0]-1, point[1]);
                        point[0] -= 1;
                        if(vit[val1][val2]) break;
                        vit[val1][val2] = true;
                        vit[val2][val1] = true;
                        answer++;
                    }
                    break;
                case 'R':
                    if(point[1]+1 <= 10){
                        val1 = getVal(point[0], point[1]);
                        val2 = getVal(point[0], point[1]+1);
                        point[1] += 1;
                        if(vit[val1][val2]) break;
                        vit[val1][val2] = true;
                        vit[val2][val1] = true;
                        answer++;
                    }
                    break;
                case 'L':
                    if(point[1]-1 >= 0){
                        val1 = getVal(point[0], point[1]);
                        val2 = getVal(point[0], point[1]-1);
                        point[1] -= 1;
                        if(vit[val1][val2]) break;
                        vit[val1][val2] = true;
                        vit[val2][val1] = true;
                        answer++;
                    }
                    break;
            }
            //System.out.println(point[0]+","+point[1]+","+answer);
        }
        return answer;
    }
    
    
}