package select;

import java.util.Scanner;

public class Sel_528 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int num = sc.nextInt();
		String minus = "minus";
		
		System.out.println(num);
		if (num < 0) {
			System.out.println(minus);
		}
	}
}
