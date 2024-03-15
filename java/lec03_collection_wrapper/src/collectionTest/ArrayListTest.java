package collectionTest;

import java.util.ArrayList;
import java.util.Collections;

public class ArrayListTest {
	public static void main(String[] args) {
		//<?> : 제네릭(이름이 없는) -> 새로운 임시 타입을 선언하는 방법
		// 어떤 타입을 지정할 지 알 수 없을 때 사용하는 기법
		// 저장할 타입에 제한을 둘 수 있다.
		// 따로 다운 캐스팅을 할 필요가 없다.
		ArrayList<Integer> datas = new ArrayList<>();
		datas.add(10);
		datas.add(20);
		datas.add(40);
		datas.add(50);
		datas.add(60);
		datas.add(80);
		datas.add(60);
		datas.add(90);
		datas.add(30);
		
//		System.out.println(datas.toString());
		
//		// 정렬(오름차순)
//		Collections.sort(datas);
//		System.out.println(datas);
//		//정렬(내림차순)
//		Collections.reverse(datas);
//		System.out.println(datas);
//		//무작위로 섞기
		Collections.shuffle(datas);
		System.out.println(datas);
		
		
		datas.add(datas.indexOf(50)+1, 500);
		datas.set(datas.indexOf(90), 9);
//		datas.remove(datas.indexOf(80));
		datas.remove(datas.get(datas.indexOf(80)));
		
		System.out.println(datas);
		
		
	}
}
