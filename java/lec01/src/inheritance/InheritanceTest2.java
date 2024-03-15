package inheritance;

public class InheritanceTest2 {
	public static void main(String[] args) {
		
	}
}

class Human{
	int data = 10;
	
	void eat() {
		System.out.println("eating");
	}
	void sleep() {
		System.out.println("sleepping");
	}
	void walk() {
		System.out.println("walking by two");
	}
}

class Monkey extends Human{
	void eatLouse() {
		System.out.println("eating Louse");
	}
	
	void walk () {
		System.out.println("walking by two or four");
	}
	
}
