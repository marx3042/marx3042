package obj;

public class EqualsTask {
	public static void main(String[] args) {
		Student std = new Student(1, "��ȯ��");
		System.out.println(std.equals(new Student(1, "��ȯ��")));
	}
}
