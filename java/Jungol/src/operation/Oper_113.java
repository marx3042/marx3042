package operation;

import java.util.Scanner;

public class Oper_113 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int wigth = sc.nextInt();
		int length = sc.nextInt();
		wigth = wigth + 5;
		length = length * 2;
		int area = wigth * length;
		String result = "wigth" + " = " + wigth + "\n" + "length" + " = " + length + "\n" + "area" + " = " + area;
		
		System.out.println(result);
		
	}
}
