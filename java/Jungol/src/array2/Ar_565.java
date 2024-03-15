package array2;

import java.util.Scanner;

public class Ar_565 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int[] arNum = new int[10];
		
		while(true) {
			int num = sc.nextInt();
			if(num == 0) break;
			arNum[num / 10]++;
		}
		for(int i = 0; i < arNum.length; i++) {
			if(!(arNum[i] == 0)) {
				System.out.println(i + " : " + arNum[i]);
			}
		}
		sc.close();
	}
}
