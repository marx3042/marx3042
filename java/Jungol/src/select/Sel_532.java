package select;

import java.util.Scanner;

public class Sel_532 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		double num1 = sc.nextDouble();
		double num2 = sc.nextDouble();
		
		if (num1 > 4.0 && num2 > 4.0) {
			System.out.println('A');
		}else if (num1 > 3.0 && num2 > 3.0) {
			System.out.println('B');
		}else {
			System.out.println('C');
		}
		sc.close();
	}
}
