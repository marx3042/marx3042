package collectionTest;

import java.util.HashSet;

public class School {
	public static void main(String[] args) {
		HashSet<Student> stdSet = new HashSet<>();
		stdSet.add(new Student(1, "jung"));
		stdSet.add(new Student(1, "jung"));
		
		System.out.println(stdSet);
//		Student std = new Student(1, "jung");
//		System.out.println(std.equals(new Student(1, "jung")));
		
		System.out.println(new Student(1, "jung").hashCode());
		System.out.println(new Student(1, "jung").hashCode());
	}
}
