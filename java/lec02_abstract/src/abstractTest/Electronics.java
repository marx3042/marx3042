package abstractTest;

public abstract class Electronics {
	private String brand;
	
	
	
	public Electronics() {
		super();
	}
	
	
	
	public String getBrand() {
		return brand;
	}



	public void setBrand(String brand) {
		this.brand = brand;
	}



	public abstract void on();
	public abstract void off();
	
	public void printBrand () {
		System.out.println(brand);
	}
	
	public final void itro () {
		System.out.println("asga");
	}
}
