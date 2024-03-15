package sync;

public class ATM implements Runnable{
	private int money = 10_000;
	
	public ATM() {
		super();
	}

	public ATM(int money) {
		super();
		this.money = money;
	}

	
	
	public int getMoney() {
		return money;
	}

	public void setMoney(int money) {
		this.money = money;
	}

	@Override
	public synchronized void run() {
		for(int i = 0; i < 5; i++) {
			withdraw(1000);
			try {
				Thread.sleep(500);
			} catch (InterruptedException e) {;}
		}
	}
	
	public /* synchronized */ void withdraw(int money) {
//		synchronized (this) {
			this.money -= money;
//		}
		
		System.out.println(Thread.currentThread().getName()+ "이(가) " + money + " 출금");
		System.out.println("현재 : " + this.money);
	}
}
