package sports;

public class Branch {
	public static void main(String[] args) {
		Nike gangnam = new Nike();
		
		gangnam.register(new FormAdapter() {

			@Override
			public String[] productList() {
				String[] menus = {"shoes", "clothes","sportsware"};
				
				return menus;
			}
		});
		
		
	}
}
