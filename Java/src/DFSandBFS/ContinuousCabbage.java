package DFSandBFS;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class ContinuousCabbage {

	static int [][] arr;
	static int count=0; //bfs countÈ½¼ö
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int numOfCase = Integer.parseInt(br.readLine());
		while(numOfCase>0) {
			StringTokenizer str = new StringTokenizer(br.readLine());
			int N = Integer.parseInt(str.nextToken());
			int M = Integer.parseInt(str.nextToken());
			int numOfCabbage = Integer.parseInt(str.nextToken());
			int num =0; // Ãâ·Â°ª
			arr = new int[N+2][M+2];
			for(int i=0;i<N+2;i++) {
				for(int j=0; j<M+2;j++) {
					arr[i][j]=0;
				}
			}
			for(int i=0;i<numOfCabbage;i++) {
				int x = Integer.parseInt(str.nextToken());
				int y = Integer.parseInt(str.nextToken());
				arr[x][y] = 1;
			}
			
			
			for(int i=1;i<=N;i++) {
				for(int j=1; j<=M;j++) {
					bfs(i,j);
					if(count>0) {
						num++;
						count=0;
					}
					
				}
			}
			System.out.println(num);
			numOfCase--;
		}
	}
	
	static void bfs(int x, int y) {
		if(arr[x][y] ==1) {
			count ++;
			arr[x][y] =0;
		}
		bfs(x+1,y);
		bfs(x-1,y);
		bfs(x,y+1);
		bfs(x,y-1);
	}
}
