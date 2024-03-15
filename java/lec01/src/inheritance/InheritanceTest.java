package inheritance;

public class InheritanceTest {
	public static void main(String[] args) {
		B b = new B();
		
		b.printData();
	}
}

class A {
	String nameA = "A";
	int data = 10;
	
	public A() {
		System.out.println("super");
	}
	
	
}

class B extends A{
	String nameB = "B";
	
	
	
	public B() {
		super();
		System.out.println("sub");
	}



	void printData() {
		System.out.println(data);
	}
}