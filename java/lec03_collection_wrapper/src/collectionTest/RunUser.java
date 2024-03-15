package collectionTest;

import java.util.ArrayList;
import java.util.Scanner;

public class RunUser {
	public static void main(String[] args) {
		// 무한 반복
		// 모든 회원가입  q 눌러 무한 입력 종료
		// 아이디 입력 받아서 데이터 유효성 검사
		// 개인정보 입력 후 데이터 베이스에 저장
		// 프로그램 종료직전에 현재 가입된 회원의 수와 회원들의 id를 출력
		Scanner sc = new Scanner(System.in);
		UserField alUser = new UserField();
		
		
		while(true) {
			System.out.println("회원가입 / q눌러 종료");
			String inputNum = sc.next();
			
			if(inputNum.equals("q")) {
				break;
			}
			
			//신규유저
			User newUser = new User();
			
			//아이디
			System.out.println("id check");
			//최적화 유의!!
			while(true) {
				String inputId = sc.next();
				
				if(alUser.overlap(inputId) == null) {
					newUser.setId(inputId);
					System.out.println("pass");
					break;
				}
				System.out.println("nonpass");
			}
			
			//회원가입후 저장
			System.out.println("password");
			newUser.setPassword(sc.next());
			
			System.out.println("name");
			newUser.setName(sc.next());
			
			System.out.println("phoneNum");
			newUser.setNumber(sc.next());
			
			alUser.newSign(newUser);
		}
		for(int i = 0; i < alUser.users.size(); i++) {
			System.out.println(alUser.users.get(i).getId());
		}
		System.out.println("가입자 수 : " + alUser.users.size());
	}
}
