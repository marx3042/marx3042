package collectionTest;

import java.util.ArrayList;
import java.util.Collections;

public class ArrayListTest {
	public static void main(String[] args) {
		//<?> : ���׸�(�̸��� ����) -> ���ο� �ӽ� Ÿ���� �����ϴ� ���
		// � Ÿ���� ������ �� �� �� ���� �� ����ϴ� ���
		// ������ Ÿ�Կ� ������ �� �� �ִ�.
		// ���� �ٿ� ĳ������ �� �ʿ䰡 ����.
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
		
//		// ����(��������)
//		Collections.sort(datas);
//		System.out.println(datas);
//		//����(��������)
//		Collections.reverse(datas);
//		System.out.println(datas);
//		//�������� ����
		Collections.shuffle(datas);
		System.out.println(datas);
		
		
		datas.add(datas.indexOf(50)+1, 500);
		datas.set(datas.indexOf(90), 9);
//		datas.remove(datas.indexOf(80));
		datas.remove(datas.get(datas.indexOf(80)));
		
		System.out.println(datas);
		
		
	}
}
