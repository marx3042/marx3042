package lec01;

public class FormatTest {
	public static void main(String[] args) {
		String name = "��ȯ��";
		int age = 25;
		final double WEIGHT = 75.5;
		
		System.out.printf("�̸� : %s",name);
		
		System.out.printf("\n���� : %d\n",age);
		System.out.printf("������ : %.1fkg",WEIGHT);
		
	}
}
