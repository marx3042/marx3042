package lec02;

class A{
	int data = 10;
	
	void printData () {
		System.out.println(data);
	}
	
	A(){
		System.out.println("hello");
	}
}


public class ClassTest {
	public static void main(String[] args) {
		A a = new A();
//		System.out.println(a);
//		a.data = 100;
		a.printData();
		a.printData();
		
	}
}
