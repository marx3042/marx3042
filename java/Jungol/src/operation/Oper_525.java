package operation;

import java.util.Scanner;

public class Oper_525 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int num1 = sc.nextInt();
		int num2 = sc.nextInt();
		int num3 = sc.nextInt();
		boolean first = (num1 > num2) && (num1 > num3);
		boolean allSame = (num1 == num2) && (num1 == num3);
		System.out.println(first + " " + allSame);
	}
}
