package annonynous;

public class Zoo {
	public static void main(String[] args) {
		Animal animal = new Animal() {

			public void eat() {
				System.out.println("dont sleeping");
				
			}

			public void sleep() {
				System.out.println("do eating");
				
			}
			
		};
	}
}
