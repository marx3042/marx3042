package obj;

public class Student {
	int num;
	String name;
	
	public Student() {;}

	public Student(int num, String name) {
		super();
		this.num = num;
		this.name = name;
	}
	
	@Override
	public String toString() {
		return this.num + " : " + this.name;
	}
	@Override
	public boolean equals(Object obj) {
		//�ּҺ�
		if(this == obj) return true;
		
		//Ÿ�Ժ�
		if(obj instanceof Student) {
			//�ٿ�ĳ����
			Student std = (Student)obj;
			if(std.num == this.num) {
				return true;
			}
		}
		return false;
	}
	 
}
