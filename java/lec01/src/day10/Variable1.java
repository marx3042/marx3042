package day10;

public class Variable1 {
	int data = 10;
	static int data_s = 20;
	
	void increaseData() {
		System.out.println(++data);
	}
	
	void increaseData_s() {
		System.out.println(++data_s);
	}
	
	public static void main(String[] args) {
		Variable1 v = new Variable1();
		
	}
}
