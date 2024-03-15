package array2;

public class Ar_570 {
	public static void main(String[] args) {
		int[][] arNum = new int[5][5];
		
		for(int i = 0 ; i < arNum.length ; i++) {
			arNum[i][0] = 1;
			arNum[0][i] = 1;
		}
		
		for(int i = 1 ; i < arNum.length ; i++) {
			for(int j = 1 ; j < arNum[0].length; j++) {
				arNum[i][j] = arNum[i-1][j] + arNum[i][j-1];
			}
		}
		
		
		
		for(int[] value : arNum) {
			for(int value2 : value) {
				System.out.print(value2 + " ");
			}
			System.out.println();
		}
	}
}
