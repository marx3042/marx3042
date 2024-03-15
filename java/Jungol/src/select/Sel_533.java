package select;

import java.util.Scanner;

public class Sel_533 {
	static final int K = 10;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		char gender = sc.next().charAt(0);
		int age = sc.nextInt();
		String result = "";
		
		
		
		
		if (gender == 'M') {
			if (age >= 18) {
				int a = 10;
				result = "MAN";
			}else {
				result = "BOY";
			}
		}else if (gender == 'F') {
			if (age >= 18) {
				result = "WOMAN";
			}else {
				result = "GIRL";
			}
		}
		System.out.println(result);
		System.out.println(K);
		sc.close();
	}
}
