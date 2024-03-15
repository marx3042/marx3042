package lec01;

import java.util.Scanner;

public class InputTest2 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.print("이름 : ");
		System.out.println(sc.nextLine()+"님 환영합니다");
		
		sc.close();
		
	}
}
