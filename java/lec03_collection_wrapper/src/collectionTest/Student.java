package collectionTest;

public class Student {
	private int num;
	private String name;
	
	public Student() {
		super();
	}

	public Student(int num, String name) {
		super();
		this.num = num;
		this.name = name;
	}

	public int getNum() {
		return num;
	}

	public void setNum(int num) {
		this.num = num;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}
	
	public boolean equals(Object obj) {
		if(this == obj) {
			return true;
		}
		if(obj instanceof Student) {
			Student std = (Student)obj;
			if(this.num == std.num) {
				return true;
			}
		}
		return false;
	}
	
	@Override
	public int hashCode() {
		
		return this.num;
	}
}
