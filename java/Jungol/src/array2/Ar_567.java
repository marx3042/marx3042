package array2;


public class Ar_567 {
	public static void main(String[] args) {
		int[][] arNum = {{5, 8, 10, 6, 4}, {11, 20, 1, 13, 2}, { 7, 9, 14, 22, 3}};
		
		for(int i = 0; i < 3; i++) {
			for(int j = 0; j < 5; j++) {
				System.out.print(String.format("   %2s", arNum[i][j]));
			}
			System.out.println();
		}
		
		
	}
}
