package lec02;

public class MethodTask {
	public static void main(String[] args) {
		MethodTask m = new MethodTask();
		
		m.ironMethod1();
		System.out.println();
		m.ironMethod2(5);
	}
	
	void ironMethod1 () {
		for(int i = 1; i <= 10; i++) {
			System.out.println(i);
		}	
	}
	void ironMethod2(int num) {
		String name = "ȫ�浿";
		for(int i = 0; i < num; i++) {
			System.out.println(name);
		}
	}
	
}
