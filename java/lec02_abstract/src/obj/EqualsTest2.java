package obj;

public class EqualsTest2 {
	public static void main(String[] args) {
		String data1 = "ABC";
		String data2 = "ABC";
		String data3 = new String("ABC");
		String data4 = new String("ABC");
		
		System.out.println(data1.equals(data2));
		System.out.println(data3.equals(data4));
		
		System.out.println(data1.toString());
		System.out.println(data2.toString());
		System.out.println(data3.toString());
		System.out.println(data4.toString());
		
	}
}
