package input;

import java.util.Scanner;

public class Ip_110 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		double yd = 91.44;
		double result;
		
		System.out.print("yard? ");
		double inputNum = sc.nextDouble();
		result = inputNum * yd;
		
		System.out.println("10.1yard = " + String.format("%.1fcm", result));
		
		
		
		sc.close();
	}
}
