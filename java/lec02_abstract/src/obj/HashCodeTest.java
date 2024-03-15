package obj;

import java.util.Random;

public class HashCodeTest {
	public static void main(String[] args) {
		Random r1 = new Random();
		Random r2 = new Random();
		
		System.out.println(r1.hashCode());
		System.out.println(r2.hashCode());
		
		r1 = r2;
		System.out.println(r1.hashCode());
		System.out.println(r2.hashCode());
	}
}
