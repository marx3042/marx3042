package collectionTest;

import java.util.HashSet;

public class SetTest {
	public static void main(String[] args) {
		HashSet<String> bloodSet = new HashSet<>();
		bloodSet.add("A");
		bloodSet.add("B");
		bloodSet.add("O");
		bloodSet.add("AB");
		bloodSet.add("AB");
		bloodSet.add("AB");
		bloodSet.add("AB");
		
		System.out.println(bloodSet.size());
		System.out.println(bloodSet);
		
	}
}
