package array2;

import java.util.Scanner;

public class Ar_569 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int[][] arNum = new int[5][4];
		int count = 0;
		
		for(int i = 0 ; i < 5 ; i++) {
			for(int j = 0 ; j < 4 ; j++) {
				arNum[i][j] = sc.nextInt();
			}
		}
		for(int i = 0 ; i < 5 ; i++) {
			int sum = 0;
			double avg = 0.0;
			String yON;
			for(int j = 0 ; j < 4 ; j++) {
				sum += arNum[i][j];
			}
			avg = sum / 4;
			if (avg >= 80) {
				yON = "pass";
				count++;
			}else {
				yON = "fail";
			}
			System.out.println(yON);
		}
		String pass = "SUccessful : ";
		System.out.println(pass + count);
		sc.close();
	}
}
