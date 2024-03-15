package bakery;

public class BreadPlate {
	
	private static BreadPlate breadPlate;
	
	int breadCount;
	int eatCount;
	
	private BreadPlate() {
		
	}
	
	public static BreadPlate getInstance() {
		if(breadPlate == null) {
			breadPlate = new BreadPlate();
		}
		return breadPlate;
	}
	
	public synchronized void makeBread() {
		if(breadCount > 9) {
			System.out.println("���� ���� á���ϴ�");
			try {
				wait();
			} catch (InterruptedException e) {;}
		}
		breadCount++;
		System.out.println("���� 1�� ��������ϴ�. ��" + breadCount + "��");
		
	}
	public synchronized void eatBread() {
		if(eatCount == 20) {
			System.out.println("���� �� ���������ϴ�.");
		}else if(breadCount < 10) {
			System.out.println("���������");
			makeBread();
		}else {
			breadCount--;
			eatCount++;
			System.out.println("���� �Ѱ� �Ծ����ϴ�. ��" + breadCount + "��");
			notify();
		}
	}
}
