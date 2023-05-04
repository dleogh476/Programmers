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