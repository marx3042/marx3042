package input;

import java.util.Scanner;

public class Ip_515 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int num1 = sc.nextInt();
		int num2 = sc.nextInt();
		int mutiply = num1 * num2;
		int divide = num1 / num2;
		
		System.out.println(num1 + " * " + num2 + " = " + mutiply);
		System.out.println(num1 + " / " + num2 + " = " + divide);
		
		sc.close();
		
		
	}
}
