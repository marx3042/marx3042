package lec01;

import java.util.Scanner;

public class Oper {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String menu = "Q. ���� �� ���ϴ� ������ ������.\n1. �����\n2. ������\n3. ������\n4. ���";
		
		System.out.println(menu);
		int color = sc.nextInt();
		String character = "";
		
		System.out.println(color);
		
		if (color == 1) {
			character = "������ ��� ����ϴ�.";
		} else if (color == 2) {
			character = "�������� ����.";
		} else if (color == 3) {
			character = "������ ������ ������.";
		} else if(color == 4){
			character = "�Ż翡 �Ĳ��ϴ�.";
		}
		
		System.out.println(character);
		
	}
}
