package lec01;

import java.util.Scanner;

public class InputTask {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println(Integer.parseInt(sc.next())+Integer.parseInt(sc.next()));
		
//		int a = sc.nextInt();
		
		sc.close();
	}
}
