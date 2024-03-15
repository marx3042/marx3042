package input;

public class Ip_513 {
	public static void main(String[] args) {
		double yd = 91.44;
		double inch = 2.54;
		
		System.out.println("2.1yd" + " = " + String.format("%.1fcm", (2.1*yd)));
		System.out.println("10.5in" + " = " + String.format("%.1fcm", (10.5*inch)));
	}
}
