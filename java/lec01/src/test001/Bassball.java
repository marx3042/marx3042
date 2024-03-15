package test001;

import java.util.Scanner;

public class Bassball {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		BassballNum myself = new BassballNum("6458");
		
		System.out.println("start");
		for(int k = 0; k < 9; k++) {
			String inputNum = sc.next();
			int strike = 0;
			int ball = 0;
			
			if(myself.inning(inputNum)) {
				System.out.println("you win");
				break;
			}else {
				for(int i = 0; i < 4; i++) {
					if(myself.countNum.charAt(i) == inputNum.charAt(i)) {
						strike++;
					} else {
						for(int j = 0; j < 4; j++) {
							if(myself.countNum.charAt(i) == inputNum.charAt(j)) {
								ball++;
							}
						}
					}	
				}
				System.out.println("strike : " + strike + "\n" + "ball : " + ball);
			}
			
		}
		
	
	}
}

class BassballNum {
	String countNum;
	
	BassballNum (String countNum){
		this.countNum = countNum;
	}
	
	boolean inning (String countNum) {
		if(this.countNum.equals(countNum)) {
			return true;
		} else {
			return false;
		}
	}
	
	
}










