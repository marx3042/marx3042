package threadTest;

public class Zoo {
	public static void main(String[] args) {
//		ThreadOn cat = new ThreadOn("�߿�");
//		ThreadOn dog = new ThreadOn("�۸�");
//		ThreadOn lion = new ThreadOn("������");
//		
//		
//		Thread catOn = new Thread(cat);
//		Thread dogOn = new Thread(dog);
//		Thread lionOn = new Thread(lion);
//		
//		catOn.start();
//		dogOn.start();
//		
//		try {
//			catOn.join();
//			dogOn.join();
//		} catch (InterruptedException e) {
//			;
//		}
//		
//		lionOn.start();
		String[] sounds = {"�߿�", "�۸�", "������"};
		ThreadOn[] animals = new ThreadOn[sounds.length];
		Thread[] threads = new Thread[sounds.length];
		
		for(int i = 0; i < sounds.length; i++) {
			animals[i] = new ThreadOn(sounds[i]);
			threads[i] = new Thread(animals[i]);
		}
		
		for(int i = 0; i < threads.length; i++) {
			threads[i].start();
			if(i != 0) {
				try {threads[i].join();} catch (InterruptedException e) {;}
			}
		}
		
		
		
		
	}
}
