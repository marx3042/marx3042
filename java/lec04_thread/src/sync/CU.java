package sync;

public class CU {
	public static void main(String[] args) {
		ATM atm = new ATM();
		
		Thread mom = new Thread(atm, "����");
		Thread son = new Thread(atm, "�ڼ�");
		
		mom.start();
		son.start();
		
	}
}
