package array2;

import java.util.Scanner;

public class Ar_564 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int[] arChar = new int[26];
		
		for(int i = 0; i < 100; i++) {
			char result = sc.next().charAt(0);
			
			if((int)result < 65 || 91 < (int)result) break;
			
			arChar[(int)result-65]++;
		}
		
		int num = 65;
		for(int i = 0; i < arChar.length; i++) {
			
			if(arChar[i]==0) {
				num++;
				continue;
			}
			String result = (char)num + " : " + arChar[i];
			System.out.println(result);
			num++;
			
		}
		
		
	}
}
