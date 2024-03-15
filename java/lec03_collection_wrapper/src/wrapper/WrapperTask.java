package wrapper;

public class WrapperTask {
	public static void main(String[] args) {
		
		int data1 = 10;
		Integer data_1 = data1;
		double data2 = 10.5;
		Double data_2 = data2;
		float data3 = 3.8F;
		Float data_3 = data3;
		char data4 = 'A';
		Character data_4 = data4;
		String data_5 = "ABC";
		boolean data6 = true;
		Boolean data_6 = data6;
		
		Object[] arList = {
				data_1,
				data2,
				(Object)data_3,
				(Object)data_4,
				(Object)data_5,
				(Object)data_6,
		};
		for(Object v : arList) {
			System.out.println(v);
		}
	}
}
