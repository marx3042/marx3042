package threadTest1;

public class ThreadTest implements Runnable{
	int inputNum;
	
	public ThreadTest() {
		super();
	}
	
	
	public void printFirst(Runnable first) {
		first.run();
	}
	public void printSecond(Runnable second) {
		second.run();
	}
	public void printThird(Runnable third) {
		third.run();
	}
	
	@Override
	public void run() {
		switch (Thread.currentThread().getName()) {
		case "1" :
			printFirst(new Runnable() {
				@Override
				public void run() {
					System.out.println("First");
				}
			});
			break;
		case "2" :
			printSecond(new Runnable() {
				@Override
				public void run() {
					System.out.println("Second");
				}
			});
			break;
		case "3" :
			printThird(new Runnable() {
				@Override
				public void run() {
					System.out.println("Third");
				}
			});
			break;
		default:
			break;
		}
		
	}
}
