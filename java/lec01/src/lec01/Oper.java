package lec01;

import java.util.Scanner;

public class Oper {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String menu = "Q. 다음 중 원하는 색깔을 고르세요.\n1. 노란색\n2. 빨간색\n3. 검은색\n4. 흰색";
		
		System.out.println(menu);
		int color = sc.nextInt();
		String character = "";
		
		System.out.println(color);
		
		if (color == 1) {
			character = "성격이 밝고 명랑하다.";
		} else if (color == 2) {
			character = "추진력이 좋다.";
		} else if (color == 3) {
			character = "차분한 성격의 소유자.";
		} else if(color == 4){
			character = "매사에 꼼꼼하다.";
		}
		
		System.out.println(character);
		
	}
}
