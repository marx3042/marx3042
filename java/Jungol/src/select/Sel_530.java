package select;

import java.util.Scanner;

public class Sel_530 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int age = sc.nextInt();
		String adult = "adult";
		String young = " years later";
		
		if (age >= 20) {
			System.out.println(adult);
		}else {
			int result = 20 - age;
			System.out.println(result + young);
		}
		
	}
}
