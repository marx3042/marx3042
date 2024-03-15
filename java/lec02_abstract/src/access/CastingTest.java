package access;


public class CastingTest {
	public static void main(String[] args) {
		Car matiz = new Car();
		SuperCar ferrari = new SuperCar();
		
		Car noOptionFerrari = new SuperCar();
//		noOptionFerrari.engineStart();
		
		SuperCar fullOptionFerrari = (SuperCar)noOptionFerrari;
//		fullOptionFerrari.openRoof();
		
		System.out.println(matiz instanceof Car);
		System.out.println(matiz instanceof SuperCar);
		System.out.println(ferrari instanceof Car);
		System.out.println(ferrari instanceof SuperCar);
		System.out.println(noOptionFerrari instanceof Car);
		System.out.println(noOptionFerrari instanceof SuperCar);
		System.out.println(fullOptionFerrari instanceof Car);
		System.out.println(fullOptionFerrari instanceof SuperCar);
		
	}
	
}

class Car {
	String brand;
	String color;
	int price;
	
	
	void engineStart() {
		System.out.println("keyON");
	}
	void engineStop() {
		System.out.println("keyOFF");
	}
	
}

class SuperCar extends Car{
	String mode;
	
	
	@Override
	void engineStart() {
		System.out.println("voiceOn");
	}
	
	void openRoof() {
		System.out.println("open");
	}
	
	void closeRoof() {
		System.out.println("close");
	}
	
}