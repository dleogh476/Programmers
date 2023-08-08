import java.util.Scanner;
public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int M = sc.nextInt();
		String deck = sc.nextLine();
		int closer = 0;
		//1.N(3 ≤ N ≤ 100), M(10 ≤ M ≤ 300,000)
		//N장에 카드 만들기
		//카드 3장 뽑기
		//3장을 더한다.
		//더한 값이 보다 M 클 경우 다시 카드 뽑음
		//같을 경우 바로 값 출력
		//closer와 비교해서 더 가까우면 closer에 저장 아니면 다시 뽑음
		int cardNum[] = new int[N];
		for(int a=0; a<N; a++) 
		{
			cardNum[a]= sc.nextInt();
		}
		int sum;
		if(N >= 3 && N<= 100) 
		{
			if(M >= 10 && M<= 300000) 
			{
			
				for(int i = 0; i < N-2; i++)
				{
					for(int j = i+1; j < N-1; j++) 
					{
						for(int s = j+1; s < N; s++) 
						{
							sum = cardNum[i]+cardNum[j]+cardNum[s];//3장을 뽑고 저장합니다.
							if(sum>M)//더한 값이 보다 M 클 경우
							{
								// 아무짓도 하지마
							}else if(sum>=closer) //closer와 비교해서 더 가까우면 closer에 저장
							{
								closer = sum;
							}
							
						}
					}
				}
				System.out.println(closer);
			}

		}

	}

}
