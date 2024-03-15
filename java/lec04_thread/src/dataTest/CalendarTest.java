package dataTest;

import java.text.SimpleDateFormat;
import java.util.Calendar;

public class CalendarTest {
	public static void main(String[] args) {
		//싱글턴 패턴
		//객체를 하나만 생성하도록 설계하며, 생성된 객체를 어디에서든지 접근할 수 있도록 한다
		Calendar today = Calendar.getInstance();
		SimpleDateFormat sdf = new SimpleDateFormat("yyy.MM.dd");
		
		today.set(2100, 11, 25);
		
		System.out.println(sdf.format(today.getTime()));
		System.out.println(today);
		
		today.get(Calendar.YEAR);
	}
}
