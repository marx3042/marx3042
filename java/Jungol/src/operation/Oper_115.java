package operation;

import java.util.Scanner;

public class Oper_115 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int minH = sc.nextInt();
		int minW = sc.nextInt();
		int kiH = sc.nextInt();
		int kiW = sc.nextInt();
		boolean result = (minH > kiH) && (minW > kiW);
		
		System.out.println(result);
		
	}
}
