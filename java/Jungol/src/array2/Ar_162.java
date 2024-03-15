package array2;

import java.util.Scanner;

public class Ar_162 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int[] arNum = new int[10];
		arNum[0] = sc.nextInt();
		arNum[1] = sc.nextInt();
		
		for(int i = 2; i < arNum.length; i++) {
			arNum[i] = (arNum[i-1] + arNum[i-2]) % 10;
		}
		
		for(int v : arNum) {
			System.out.print(v + " ");
		}
		
		sc.close();
		
	}
}
