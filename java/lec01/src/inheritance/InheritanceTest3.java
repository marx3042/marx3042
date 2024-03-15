package inheritance;

public class InheritanceTest3 {
	public static void main(String[] args) {
		SuperCar ferrari = new SuperCar();
		
		ferrari.engineStart();
		ferrari.engineStop();
		
	}
}

class Car {
	String brand;
	String color;
	int price;
	
	Car() {}
	
	public Car(String brand, String color, int price) {
		this.brand = brand;
		this.color = color;
		this.price = price;
	}
	
	void engineStart() {
		System.out.println("keyON");
	}
	void engineStop() {
		System.out.println("keyOFF");
	}
	
}

class SuperCar extends Car{
	String mode;
	
	public SuperCar() {}

	public SuperCar(String brand, String color, int price, String mode) {
		super(brand, color, price);
		this.mode = mode;
	}
	
	@Override
	void engineStart() {
		super.engineStart();
		System.out.println("voiceOn");
	}
	
	@Override
	void engineStop() {
		System.out.println("voiceOff");
	}
}