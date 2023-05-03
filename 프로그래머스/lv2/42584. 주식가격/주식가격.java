class Solution {
    public int[] solution(int[] prices) {
        int[] answer = new int[prices.length];
        for(int idx=0; idx < prices.length; idx++){
            int count = 0;
            for(int point = idx+1; point < prices.length; point++){
                count += 1;
                if(prices[idx] > prices[point]){
                    break;
                }
            }
            //System.out.println(count);
            answer[idx] = count;
        }
        return answer;
    }
}