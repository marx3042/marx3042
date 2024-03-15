package sync;

public class CU {
	public static void main(String[] args) {
		ATM atm = new ATM();
		
		Thread mom = new Thread(atm, "엄마");
		Thread son = new Thread(atm, "자손");
		
		mom.start();
		son.start();
		
	}
}
