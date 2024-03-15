package lec02;

import java.util.Random;

public class RandomTest {
	public static void main(String[] args) {
		Random r = new Random();
		
		System.out.println(r.nextInt(100));
		System.out.println(r.nextInt());
		System.out.println(r.nextInt());
		System.out.println(r.nextInt());
		System.out.println(r.nextInt());
		System.out.println(r.nextInt());
		
		AA.a();
		
	}
}

class AA {
	public static void a() {
		System.out.println("hi");
	}
}

