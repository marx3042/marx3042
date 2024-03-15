package dataTest;

import java.text.SimpleDateFormat;
import java.util.Date;

public class DateTest {
	public static void main(String[] args) {
		Date today = new Date();
		SimpleDateFormat sdf = new SimpleDateFormat("yyyy.MM.dd EEEE");
		
		
		today.setYear(98);	// 1900년부터 시작점이기 때문에 전달한 정수를 더하여 년도가 설정
		today.setMonth(9);	// 월은 index로 구성
		today.setDate(1);
		today.getDay();		//일 ~ 토까지 indexNumber로 구성
		
		System.out.println(today);
		System.out.println(sdf.format(today));
		
	}
}
