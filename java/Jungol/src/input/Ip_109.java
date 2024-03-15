package input;

import java.util.Scanner;

public class Ip_109 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int num1 = sc.nextInt();
		int num2 = sc.nextInt();
		int num3 = sc.nextInt();
		int sum = num1 + num2 + num3;
		
		System.out.println("sum = " +sum);
		
		sc.close();
	}
}
