package collectionTest;

import java.util.ArrayList;
import java.util.Scanner;

public class RunUser {
	public static void main(String[] args) {
		// ���� �ݺ�
		// ��� ȸ������  q ���� ���� �Է� ����
		// ���̵� �Է� �޾Ƽ� ������ ��ȿ�� �˻�
		// �������� �Է� �� ������ ���̽��� ����
		// ���α׷� ���������� ���� ���Ե� ȸ���� ���� ȸ������ id�� ���
		Scanner sc = new Scanner(System.in);
		UserField alUser = new UserField();
		
		
		while(true) {
			System.out.println("ȸ������ / q���� ����");
			String inputNum = sc.next();
			
			if(inputNum.equals("q")) {
				break;
			}
			
			//�ű�����
			User newUser = new User();
			
			//���̵�
			System.out.println("id check");
			//����ȭ ����!!
			while(true) {
				String inputId = sc.next();
				
				if(alUser.overlap(inputId) == null) {
					newUser.setId(inputId);
					System.out.println("pass");
					break;
				}
				System.out.println("nonpass");
			}
			
			//ȸ�������� ����
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
		System.out.println("������ �� : " + alUser.users.size());
	}
}
