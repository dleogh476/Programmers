class Solution {
    int solution(int[][] land) {
        int answer = 0;
        for(int idx = 1; idx < land.length; idx++){
            land[idx][0] += Math.max(land[idx-1][1],Math.max(land[idx-1][2],land[idx-1][3]));
            land[idx][1] += Math.max(land[idx-1][0],Math.max(land[idx-1][2],land[idx-1][3]));
            land[idx][2] += Math.max(land[idx-1][0],Math.max(land[idx-1][1],land[idx-1][3]));
            land[idx][3] += Math.max(land[idx-1][0],Math.max(land[idx-1][1],land[idx-1][2]));
        }
        for(int idx = 0; idx < 4; idx++){
            answer = Math.max(answer, land[land.length-1][idx]);
        }
        return answer;
    }
    
}

/*
class Solution {
    int solution(int[][] land) {
        int answer = 0;
        //DFS
        //1. 첫번째 행은 모든 요소들의 모두 DFS함
        //2. 가장 큰 값을 찾기 위해서 나온 모든 값 비교
        int val = 0;        
        for(int idx = 0; idx < 4; idx++){
            val = DFS(land, 0, idx,land.length);
            //System.out.println(land.length);
            if(val > answer){
                answer = val;
            }
        }
        return answer;
    }
    
    int DFS(int[][] land, int row, int col, int land_row_size){
        int ret = land[row][col];
        //맨 마지막 행일 경우 선택한 위치 결과 값 리턴
        if(row >= land_row_size-1){
            return ret;
        }
        int val = 0;
        for(int col_idx = 0; col_idx < 4; col_idx++){
            if (col_idx != col){
                int r = DFS(land, row + 1, col_idx,land_row_size);
                if(r > val){
                    val = r;
                }
            }
        }
        ret += val;
        return ret;
    }
}
*/