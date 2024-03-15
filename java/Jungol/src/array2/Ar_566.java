package array2;

import java.util.Scanner;

public class Ar_566 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int[] arNum = new int[100];
		arNum[0] = 100;
		arNum[1] = sc.nextInt();
		System.out.print(arNum[0] + " " + arNum[1]);
		for(int i = 2; i < arNum.length; i++) {
			arNum[i] = arNum[i-2] - arNum[i - 1];
			System.out.print(" " + arNum[i]);
			if(arNum[i] < 0) break;
		}
		
		sc.close();
	}
}
