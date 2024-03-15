package collectionTest;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.Iterator;

public class HashSetTest {
	public static void main(String[] args) {
		HashSet<String> fruitSet = new HashSet<>();
		fruitSet.add("watermelon");
		fruitSet.add("peach");
		fruitSet.add("manggo");
		fruitSet.add("strewvery");
		fruitSet.add("apple");
		fruitSet.add("apple");
		fruitSet.add("apple");
		
		System.out.println(fruitSet.toString());
		System.out.println(fruitSet.contains("apple"));
		
		ArrayList<String> fruitList = new ArrayList<>(fruitSet);
		
		
//		Iterator<String> iter = fruitSet.iterator();
//		while(iter.hasNext()) {
//			System.out.println(iter.next());
//		}
	}
}
