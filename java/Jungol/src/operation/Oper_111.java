package operation;

import java.util.Scanner;

public class Oper_111 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int kor = sc.nextInt();
		int eng = sc.nextInt();
		int mat = sc.nextInt();
		int com = sc.nextInt();
		int sum = kor + eng + mat + com;
		int avg = sum / 4;
		String sumSt = "sum ";
		String avgSt = "avg ";
		System.out.println(sumSt + sum + "\n" + avgSt + avg);
	}
}
