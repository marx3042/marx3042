package operation;

import java.util.Scanner;

public class Oper_112 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int num1 = sc.nextInt();
		int num2 = sc.nextInt();
		int share = num1 / num2;
		int divide = num1 % num2;
		String result = num1 + " / " + num2 + " = " + share + "..." + divide;
		
		System.out.println(result);
		
		
	}
}
