package lec02;

public class Road {
	public static void main(String[] args) {
		Car momCar = new Car("Benz", "Black", 10_000);
		Car daddyCar = new Car("BMW", "Blue", 8000);
		Car myCar = new Car(600);
		
		
		
	}
}

class Car {
	// variable
	String brand;
	String color;
	int price;
	
	// construct
	Car(String brand, String color, int price){
		this.brand = brand;
		this.color = color;
		this.price = price;
	}
	
	Car(int price){
		this.price = price;
	}
	
	// method
	void engineStart() {
		System.out.println(this.brand + "on");
	}
	
	void engineStop() {
		System.out.println(this.brand + "stop");
	}
	
}