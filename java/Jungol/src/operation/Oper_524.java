package operation;

import java.util.Scanner;

public class Oper_524 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		boolean num1 = sc.nextInt() != 0;
		boolean num2 = sc.nextInt() != 0;
		
		System.out.println((num1 && num2) + " " + (num1 || num2));
		
		
	}
}
