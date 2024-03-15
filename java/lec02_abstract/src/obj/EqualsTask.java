package obj;

public class EqualsTask {
	public static void main(String[] args) {
		Student std = new Student(1, "정환용");
		System.out.println(std.equals(new Student(1, "정환용")));
	}
}
