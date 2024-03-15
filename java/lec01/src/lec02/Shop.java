package lec02;

import java.util.Scanner;

public class Shop {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		SuperCar myCar = new SuperCar("","",100,"1234");
		String menu = "1.on 2.off 3.bye";
		
		while(true) {
			System.out.println(menu);
			char inputChar = sc.next().charAt(0);
			if(menu.split(" ")[0].charAt(0) == inputChar) {
				System.out.println("go");
				if(!myCar.check) {
					for(int i = 0; i < 4; i++) {
						if(i < 3) {
							if(myCar.passwordOn(sc.next())) {
								myCar.start();
								break;
							}else {
								System.out.println("replay");
								continue;
							}
						}else {
							System.out.println("°æÂû Ãâµ¿");
						}
					}
				}else {
					myCar.start();
				}
			} else if(menu.split(" ")[1].charAt(0) == inputChar) {
				myCar.stop();
			} else if(menu.split(" ")[2].charAt(0) == inputChar){
				System.out.println("bye");
				break;
			}else {
				System.out.println("choose again");
			}
		}
		
	
	sc.close();
	}
}

class SuperCar {
	String brand;
	String color;
	int price;
	boolean check;
	String password = "0000";
	
	public SuperCar(String brand, String color, int price, String password) {
		super();
		this.brand = brand;
		this.color = color;
		this.price = price;
		this.password = password;
	}
	
	void start() {
		if(!this.check) {
			this.check = true;
			System.out.println("on");
		}else {
			System.out.println("already start");
		}
	}
	
	void stop () {
		if(this.check) {
			this.check = false;
			System.out.println("stop");
		}else {
			System.out.println("already stop");
		}
	}
	
	boolean passwordOn(String password) {
		if(this.password.equals(password)) {
			return true;
		}else {
			return false;
		}
		
		
	}
		
	
}