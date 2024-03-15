package threadTest1;

import java.util.Scanner;

public class MainThreadTest {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int[] inputNum = new int[3];
		ThreadTest t = new ThreadTest();
		Thread[] arThread = new Thread[3];
		
		for(int i = 0; i < inputNum.length;i++) {
			arThread[i] = new Thread(t);
		}
		
		System.out.print("ют╥б : ");
		for(int i = 0; i < inputNum.length; i++) {
			inputNum[i] = sc.nextInt();
			arThread[i].setName(inputNum[i] + "");
		}
		
		for(int i = 0; i < arThread.length; i++) {
			arThread[i].start();
			try {
				arThread[i].join();
			} catch (InterruptedException e) {}
		}
		
		sc.close();
	}
}
