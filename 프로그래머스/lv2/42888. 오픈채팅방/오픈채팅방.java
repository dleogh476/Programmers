import java.util.*;

class Solution {//명령어 
    public String[] solution(String[] record) {
        String[] answer = {};
        //Key id, Key name
        HashMap<String, String> user = new HashMap<>();
        Queue<String[]> result = new LinkedList<>();
        
        for(String c:record){
            String[] commends = c.split(" ");
            switch(commends[0]){
                case "Enter":
                    user.put(commends[1], commends[2]);
                    String[] newreult1 = {commends[1], 
                                          "님이 들어왔습니다."};
                    result.add(newreult1);
                    break;
                case "Leave":
                    String[] newreult2 = {commends[1], 
                                          "님이 나갔습니다."};
                    result.add(newreult2);
                    break;
                case "Change":
                    user.replace(commends[1], commends[2]);
                    break;
            }
            
        }
        //System.out.println(Arrays.toString(result.remove()));
        int r_size = result.size();
        for(int idx = 0; idx < r_size; idx++){
            String[] r = result.remove();
            String m = String.format("%s%s",user.get(r[0]),
                                     r[1]);
            answer = Arrays.copyOf(answer, answer.length+1);
            answer[answer.length -1] = m;
        }
        
        return answer;
    }
}