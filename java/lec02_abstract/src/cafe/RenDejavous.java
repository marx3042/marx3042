package cafe;

public class RenDejavous {
	public String branchName;
	
	public void register(Form form) {
		String[] menus = form.getMenu();
		System.out.println(branchName + "menu");
		
		for (int i = 0; i < menus.length; i++) {
			System.out.println(menus[i]);
		}
		form.sell("ice americano");
	}
}
