package operation;

import java.util.Scanner;

public class Oper_114 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int num1 = sc.nextInt();
		int num2 = sc.nextInt();
		
		System.out.println(String.format("%s",(++num1)) + " " + String.format("%s",(num2--)));
		System.out.println(String.format("%s", num1) + " " + String.format("%s", num2));
	}
}
