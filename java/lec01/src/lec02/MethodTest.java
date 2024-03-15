package lec02;

public class MethodTest {
	public static void main(String[] args) {
		MethodTest m = new MethodTest();
		int a = 10;
		
		System.out.println(m.plus(a));
		
	}
	
	int plus (int num) {
		int result = 0;
		for(int i = 1; i <= num; i++) {
			result += i;
		}
		
		return result;
	}
}
