package array2;

public interface Ar_163 {
	public static void main(String[] args) {
		int[][] arNum = {
				{3, 5, 9}, 
				{2, 11, 5}, 
				{8, 30, 10}, 
				{22, 5, 1}
		};
		int num = 0;
		for(int[] v : arNum) {
			for(int vi : v) {
				num += vi;
				System.out.print(vi + " ");
			}
			System.out.println();
		}
		System.out.println(num);
	}
}
