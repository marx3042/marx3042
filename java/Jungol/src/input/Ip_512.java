package input;

public class Ip_512 {
	public static void main(String[] args) {
		int weight = 49;
		double gravity = 0.2683;
		double result = weight * gravity;
		
		System.out.println(weight + " * " + String.format("%f", gravity) + " = " + String.format("%f", result));
	}
}
