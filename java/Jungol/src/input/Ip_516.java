package input;

import java.util.Scanner;

public class Ip_516 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		double num1 = sc.nextDouble();
		double num2 = sc.nextDouble();
		String one = sc.next();
		
		System.out.println(String.format("%.2f", num1) + "\n" + String.format("%.2f", num2) + "\n" + one);
		
		sc.close();
	}
}
