package dataTest;

import java.text.SimpleDateFormat;
import java.util.Calendar;

public class CalendarTest {
	public static void main(String[] args) {
		//�̱��� ����
		//��ü�� �ϳ��� �����ϵ��� �����ϸ�, ������ ��ü�� ��𿡼����� ������ �� �ֵ��� �Ѵ�
		Calendar today = Calendar.getInstance();
		SimpleDateFormat sdf = new SimpleDateFormat("yyy.MM.dd");
		
		today.set(2100, 11, 25);
		
		System.out.println(sdf.format(today.getTime()));
		System.out.println(today);
		
		today.get(Calendar.YEAR);
	}
}
