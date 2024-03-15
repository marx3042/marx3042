package exceptionTest;

import java.util.InputMismatchException;
import java.util.Scanner;

public class ExceptionTask {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int[] arNum = new int[5];
		int i = 0;
		
		 while(true) {
			String temp = sc.next();
			if(temp.equals("q")) break;
			
			try {
				arNum[i] = Integer.parseInt(temp);
				i++;
			} catch(NumberFormatException e) {
				System.out.println("틀려써");
			} catch(ArrayIndexOutOfBoundsException e) {
				System.out.println("넘쳐써");
			} catch(Exception e) {
				System.out.println(e);
			}
			
		 }
		for(int v : arNum) {
			System.out.println(v);
		}
	 }
}

