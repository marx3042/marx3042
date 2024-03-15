package array2;

import java.util.Scanner;

public class Ar_168 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int[][] arNum = new int[10][10];
		int length = sc.nextInt();
		
		
		for(int i = 0; i < length; i++) {
			arNum[i][0] = 1;
			for(int j = 0; j <= i; j++) {
				if(j == 0) continue;
				if(j == i) {
					arNum[i][j] = 1;
					continue;
				}
				arNum[i][j] = arNum[i-1][j-1] + arNum[i-1][j];
			}
		}
		for(int i = 0; i < arNum.length; i++) {
			for(int j = 0; j < arNum[0].length; j++) {
				if(arNum[i][j] == 0) continue;
				System.out.print(arNum[i][j] + " ");
			}
			System.out.println();
		}
	}
}
