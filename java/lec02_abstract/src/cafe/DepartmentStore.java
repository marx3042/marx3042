package cafe;

public class DepartmentStore {
	public static void main(String[] args) {
		RenDejavous gangnam = new RenDejavous();
		gangnam.branchName = "°­³²Á¡";
		gangnam.register(new Form() {
			
			public String[] getMenu() {
				String[] menus = {"ice americano", "cafelatte", "mocalatte"};
				return menus;
			}

			public void sell(String order) {
				String[] menus = getMenu();
				for(int i = 0; i < menus.length; i++) {
					System.out.println(order + "clear");
				}
				
			}
			
		});
	}
}
