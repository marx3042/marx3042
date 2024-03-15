package lec02;

import java.util.Scanner;

public class MethodTask2 {
	public static void main(String[] args) {
		MethodTask2 m = new MethodTask2();
		Scanner sc = new Scanner(System.in);
		/*
		 * String inputSt = sc.next(); char inputChar = 'p';
		 * 
		 * System.out.println(m.count(inputSt, inputChar));
		 */
		String[] number = new String[5];
		
		/*
		 * for(int i = 0; i < number.length; i++) { number[i] = String.format("%s",
		 * sc.nextInt()); // String.valueOf(sc.nextInt()); }
		 * System.out.println(m.result(number, 2));
		 * 
		 * int[] arData = new int[5]; for(int i = 0; i < arData.length; i++) { arData[i]
		 * = sc.nextInt(); }
		 */
		
		m.change("°øÀÏ°ø»ï°ø»çÀÌ»ïÀ°¿À»ï");
		
		
		
		
		sc.close();
		
	}
	
	int count(String name, char inputChar) {
		int count = 0;
		for(int i = 0; i < name.length(); i++) {
			if(name.split("")[i].charAt(0) == inputChar) {
				count++;
			}
		}
		
		return count;
	}
	
	String result(String[] num, int index) {
		String temp;	
		
			temp = num[index-1];
			
		return temp;
	}
	
	void change (String number) {
		String arResult = "°øÀÏÀÌ»ï»ç¿ÀÀ°Ä¥ÆÈ±¸";
		
		for(int i = 0; i < number.length(); i++) {
			System.out.print(arResult.indexOf(number.charAt(i)));
		}
		
		/*for(int i = 0; i < number.length(); i++) {
			if(number.split("")[i].charAt(0) == '°ø') {
				arResult[i] = 0;
			}else if(number.split("")[i].charAt(0) == 'ÀÏ') {
				arResult[i] = 1;
			}else if(number.split("")[i].charAt(0) == 'ÀÌ') {
				arResult[i] = 2;
			}else if(number.split("")[i].charAt(0) == '»ï') {
				arResult[i] = 3;
			}else if(number.split("")[i].charAt(0) == '»ç') {
				arResult[i] = 4;
			}else if(number.split("")[i].charAt(0) == '¿À') {
				arResult[i] = 5;
			}else if(number.split("")[i].charAt(0) == 'À°') {
				arResult[i] = 6;
			}else if(number.split("")[i].charAt(0) == 'Ä¥') {
				arResult[i] = 7;
			}else if(number.split("")[i].charAt(0) == 'ÆÈ') {
				arResult[i] = 8;
			}else if(number.split("")[i].charAt(0) == '±¸') {
				arResult[i] = 9;
			}
		}*/
		
		
	}
}
