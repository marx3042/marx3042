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
		//주소비교
		if(this == obj) return true;
		
		//타입비교
		if(obj instanceof Student) {
			//다운캐스팅
			Student std = (Student)obj;
			if(std.num == this.num) {
				return true;
			}
		}
		return false;
	}
	 
}
