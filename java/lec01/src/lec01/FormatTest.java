package lec01;

public class FormatTest {
	public static void main(String[] args) {
		String name = "정환용";
		int age = 25;
		final double WEIGHT = 75.5;
		
		System.out.printf("이름 : %s",name);
		
		System.out.printf("\n나이 : %d\n",age);
		System.out.printf("몸무게 : %.1fkg",WEIGHT);
		
	}
}
