package lec02;

public class StringTest {
	public static void main(String[] args) {
		String data = "ABC";
		String data2 = "10,20,30";
		
		System.out.println(data2.length());
		System.out.println(data2.split(",").length);
		System.out.println(data2.split(",").toString());
		
	}
}
