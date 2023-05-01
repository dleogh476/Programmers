import java.util.PriorityQueue;

class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;
        PriorityQueue<Integer> lowheap = new PriorityQueue<>();
        for (int num: scoville){
            lowheap.add(num);
        }
        //System.out.println(lowheap);
        while(lowheap.peek() < K){
            int num1, num2, mix;
            if(lowheap.size() <= 1){
                return -1;
            }
            num1 = lowheap.poll(); num2 = lowheap.poll();
            //System.out.println(lowheap);
            mix = num1 + (2*num2);
            lowheap.add(mix);
            answer += 1;
            //System.out.println(lowheap);
        }
        
        return answer;
    }
}