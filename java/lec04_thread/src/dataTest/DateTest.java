package dataTest;

import java.text.SimpleDateFormat;
import java.util.Date;

public class DateTest {
	public static void main(String[] args) {
		Date today = new Date();
		SimpleDateFormat sdf = new SimpleDateFormat("yyyy.MM.dd EEEE");
		
		
		today.setYear(98);	// 1900����� �������̱� ������ ������ ������ ���Ͽ� �⵵�� ����
		today.setMonth(9);	// ���� index�� ����
		today.setDate(1);
		today.getDay();		//�� ~ ����� indexNumber�� ����
		
		System.out.println(today);
		System.out.println(sdf.format(today));
		
	}
}
