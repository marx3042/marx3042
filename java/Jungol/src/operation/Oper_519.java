package operation;

import java.util.Scanner;

public class Oper_519 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int firstNum = sc.nextInt();
		int finalNum = sc.nextInt();
		int first = firstNum + 100;
		int second = finalNum % 10;
		
		System.out.println(first + "\n" + second);
		
		
	}
}
