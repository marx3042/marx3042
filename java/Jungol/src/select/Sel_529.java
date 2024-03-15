package select;

import java.util.Scanner;

public class Sel_529 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int length = sc.nextInt();
		int wigth = sc.nextInt();
		int ob = wigth + 100 - length;
		String obSt = "Obesity";
		
		System.out.println(ob);
		if (ob > 0) {
			System.out.println(obSt);
		}
		
	}
}
