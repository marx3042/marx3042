package thread;

public class ThreadTest {
	//main�޼ҵ�� ���α׷��� ������ִ� �޼ҵ�
	public static void main(String[] args) {
		Thread2 t1 = new Thread2();
		Thread2 t2 = new Thread2();
		
		Thread thread1 = new Thread(t1, "?");
		Thread thread2 = new Thread(t2, "!");
		
		thread1.start();
		thread2.start();
		
		//join() ����� ��ü�� �����尡 ��� ����Ǿ�� �ٸ� �����尡 ����
		try {
			thread1.join();
			thread1.join();
		} catch (InterruptedException e) {
			;
		}
		
		System.out.println("main stop");
		
//		Thread1 t1 = new Thread1("��");
//		Thread1 t2 = new Thread1("��");
//		
//		t1.start();
//		t2.start();
		
//		t1.run();
//		t2.run();
	}
}
