package collectionTest;

import java.util.HashMap;
import java.util.Iterator;
import java.util.Map.Entry;

public class HashMapTest {
	public static void main(String[] args) {
		HashMap<String , Integer> fruitMap = new HashMap<>();
		fruitMap.put("apple", 1500);
		fruitMap.put("peach", 500);
		fruitMap.put("melon", 2000);
		fruitMap.put("watermelon", 8000);
		fruitMap.put("banana", 1500);
		
		System.out.println(fruitMap);
		System.out.println(fruitMap.get("apple"));
		System.out.println(fruitMap.size());
		
		double sum = 0.0;
		for(int price : fruitMap.values()) {
			sum += price;
		}
		System.out.println(sum/fruitMap.size());
		
//		Iterator<String> iter = fruitMap.keySet().iterator();
//		while(iter.hasNext()) {
//			System.out.println(iter.next());
//		}
		
//		Iterator<Entry<String, Integer>> iter = fruitMap.entrySet().iterator();
//		
//		while(iter.hasNext()) {
//			Entry<String, Integer> entry = iter.next();
//			
//			System.out.print(entry.getKey() + ",");
//			System.out.println(entry.getValue());
//		}
	}
}
