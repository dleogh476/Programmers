import java.util.Queue;
import java.util.LinkedList;
class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        int answer = 0;
        int sum = 0;
        Queue<Integer> q = new LinkedList<Integer>();
        for(int w:truck_weights)
        {
            while(true)
            {
                if(q.isEmpty())
                {
                    q.add(w);
                    sum+=w;
                    answer++;
                    break;
                }else if(q.size() == bridge_length)
                {
                    sum -=q.poll();
                }else if(sum+w>weight)
                {
                    q.add(0);
                    answer++; 
                }else
                {
                    q.add(w);
                    sum+=w;
                    answer++;
                    break;
                }
            }
            
        }
        return answer+bridge_length;
    }
}