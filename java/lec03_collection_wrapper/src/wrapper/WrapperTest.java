package wrapper;

public class WrapperTest {
	public static void main(String[] args) {
		int data_i = 10;
		
		Integer data_I = data_i; //auto boxing
		data_i = data_I; // auto unboxing
		
//		//boxing
//	//	Integer data_I = new Integer(data_i);
//		Integer data_I = Integer.valueOf(data_i);
//		
//		//unboxing
//		data_i = data_I.intValue();
	}
}
