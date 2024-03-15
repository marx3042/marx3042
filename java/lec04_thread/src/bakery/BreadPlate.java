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
			System.out.println("»§ÀÌ °¡µæ Ã¡½À´Ï´Ù");
			try {
				wait();
			} catch (InterruptedException e) {;}
		}
		breadCount++;
		System.out.println("»§À» 1°³ ¸¸µé¾ú½À´Ï´Ù. ÃÑ" + breadCount + "°³");
		
	}
	public synchronized void eatBread() {
		if(eatCount == 20) {
			System.out.println("»§ÀÌ ´Ù ¶³¾îÁ³½À´Ï´Ù.");
		}else if(breadCount < 10) {
			System.out.println("»§¸¸µé±âÁß");
			makeBread();
		}else {
			breadCount--;
			eatCount++;
			System.out.println("»§À» ÇÑ°³ ¸Ô¾ú½À´Ï´Ù. ÃÑ" + breadCount + "°³");
			notify();
		}
	}
}
