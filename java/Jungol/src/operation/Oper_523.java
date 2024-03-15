package operation;

import java.util.Scanner;

public class Oper_523 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int num1 = sc.nextInt();
		int num2 = sc.nextInt();
		String line1 = num1 + " > " + num2 + " --- ";
		String line2 = num1 + " < " + num2 + " --- ";
		String line3 = num1 + " >= " + num2 + " --- ";
		String line4 = num1 + " <= " + num2 + " --- ";
		System.out.println(line1 + (num1 > num2));
		System.out.println(line2 + (num1 < num2));
		System.out.println(line3 + (num1 >= num2));
		System.out.println(line4 + (num1 <= num2));
		
	}
}
