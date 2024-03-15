package sports;

import cafe.Form;

public class Nike {
	public String branchName;
	
	Nike() {
		super();
	}
	
	Nike(String branchName){
		super();
		this.branchName = branchName;
	}
	
	public void register(Menur form) {
		String[] menus = form.productList();
		
		System.out.println(branchName + "menu");
		for(String v : menus) {
			System.out.println(v);
		}
		
		if(form instanceof FormAdapter) {
			System.out.println("distrebutting free");
		}
		
	}
}
