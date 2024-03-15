package wrapper;

import java.util.ArrayList;
import java.util.Collections;

public class ArTest {
	public static void main(String[] args) {
		// 1
		ArrayList<Integer> al_1 = new ArrayList<Integer>();
		
		for(int i = 1; i <= 10; i++) {
			al_1.add(i);
		}
		System.out.println(al_1);
		
		// 2
		ArrayList<Integer> al_2 = new ArrayList<Integer>();
		
		for(int i = 1; i <= 50; i++) {
			al_2.add(i * 2);
		}
		System.out.println(al_2);
		
		// 3
		ArrayList<Character> al_3 = new ArrayList<Character>();
		
		for(int i = 0; i < 6; i++) {
			al_3.add((char)(65 + i));
		}
		System.out.println(al_3);
		
		// 4
		ArrayList<Character> al_4 = new ArrayList<Character>();
		
		for(int i = 0; i < 5; i++) {
			al_4.add((char)(65 + (2 < i ? i + 1 : i)));
		}
		System.out.println(al_4);
		
		// 5
		ArrayList<Integer> al_5 = new ArrayList<Integer>();
		
		al_5.add(23);
		al_5.add(45);
		al_5.add(123);
		al_5.add(4532);
		al_5.add(3);
		
		System.out.println(Collections.max(al_5) + " " + Collections.min(al_5));
		
		// 6
		ArrayList<String> al_6 = new ArrayList<String>();
		
		al_6.add("Apple");
		al_6.add("banana");
		al_6.add("Melon");
		
		for(String v : al_6) {
			if(65 <= (int)v.charAt(0) && (int)v.charAt(0) < 91) {
				System.out.println(v);
			}
		}
	}
}
