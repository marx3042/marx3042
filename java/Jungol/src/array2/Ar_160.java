package array2;

import java.util.Scanner;

public class Ar_160 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int[] arNum = new int[6];
		
		for(int i = 0 ; i < 10; i++) {
			arNum[sc.nextInt()-1]++;
		}
		
		for(int i = 0 ; i < 6 ; i++) {
			System.out.println((i+1) + " : " + arNum[i]);
		}
		
		sc.close();
	}
}
