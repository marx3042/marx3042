package operation;

import java.util.Scanner;

public class Oper_518 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int num1 = sc.nextInt();
		int num2 = sc.nextInt();
		int num3 = sc.nextInt();
		int sum = num1 + num2 + num3;
		double avg = sum / 3;
		String result = "sum : "+sum + "\navg : " + (int)avg;
		System.out.println(result);
		
	}
}
