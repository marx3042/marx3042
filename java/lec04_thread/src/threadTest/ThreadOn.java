package threadTest;

public class ThreadOn implements Runnable{
	String data;
	
	
	
	public ThreadOn() {
		super();
	}

	public ThreadOn(String data) {
		this.data = data;
	}

	@Override
	public void run() {
		for(int i = 0; i < 10; i++) {
			try {
				Thread.sleep(100);
			} catch (Exception e) {
				;
			}
			System.out.println(data);
		}
		
	}
}
