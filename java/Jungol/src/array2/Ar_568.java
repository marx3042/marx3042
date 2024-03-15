package array2;

import java.util.Scanner;

public class Ar_568 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int[][] arNum1 = new int[2][4];
		int[][] arNum2 = new int[2][4];
		
		String first = "first array";
		System.out.println(first);
		for(int i = 0; i < 2; i++) {
			for(int j = 0; j < 4; j++) {
				arNum1[i][j] = sc.nextInt();
			}
		}
		String second = "second array";
		System.out.println(second);
		for(int i = 0; i < 2; i++) {
			for(int j = 0; j < 4; j++) {
				arNum2[i][j] = sc.nextInt();
			}
		}
		
		for(int i = 0 ; i < 2 ; i++) {
			for(int j = 0 ; j < 4 ; j++) {
				int num = arNum1[i][j] * arNum2[i][j];
				System.out.print(num + " ");
			}
			System.out.println();
		}
	
	sc.close();
	}
}
