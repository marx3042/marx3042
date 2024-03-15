package select;

import java.util.Scanner;

public class Sel_531 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		double wigth = sc.nextDouble();
		
		if (wigth > 88.45) {
			System.out.println("Heavyweight");
		}else if (wigth <= 88.45) {
			System.out.println("Cruiserweight");
		}else if (wigth <= 72.57) {
			System.out.println("Middleweight");
		}else if (wigth <= 61.23) {
			System.out.println("Lightweight");
		}else if (wigth <= 50.80) {
			System.out.println("Flyweight");
		}
	}
}
