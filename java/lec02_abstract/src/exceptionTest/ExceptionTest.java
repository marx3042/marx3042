package exceptionTest;

import java.util.InputMismatchException;
import java.util.Scanner;

public class ExceptionTest {
	public static void main(String[] args) {
//		try {
//			System.out.println(10 / 0);
//		} catch (Exception e) {
//			System.out.println("sksnstndjqtdma");
//		}
		Scanner sc = new Scanner(System.in);
		int[] arData = new int[5];

		try {
			arData[0] = sc.nextInt();
		} catch (InputMismatchException e) {
			System.out.println("asdfasdfsdf");
		}catch (Exception e) {
			System.out.println(e);
		}			
		
		System.out.println("asd");
	}
}
