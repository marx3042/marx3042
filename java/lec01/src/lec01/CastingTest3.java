package lec01;

public class CastingTest3 {
	public static void main(String[] args) {
		System.out.println(1 + "2" + 3);
		System.out.println(Integer.parseInt("1")+9+2);
		System.out.println(Double.parseDouble("1.5")+0.5);
		
		System.out.println(Double.parseDouble(String.format("%.2f",Math.PI))+1.1);
		
	}
}
