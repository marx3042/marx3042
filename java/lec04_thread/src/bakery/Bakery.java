package bakery;

import javax.swing.JOptionPane;

public class Bakery {
	public static void main(String[] args) {
		BreadMaker makerThread = new BreadMaker();
		Thread maker = new Thread(makerThread);
		String[] btns = {"�� �Ա�", "������"};
		int chioce = 0;
		
		maker.start();
		
		while(true) {
			chioce = JOptionPane.showOptionDialog(null, "", "����", JOptionPane.DEFAULT_OPTION,
					JOptionPane.PLAIN_MESSAGE, null, btns, null);
			if(chioce == 0) {
				BreadPlate.getInstance().eatBread();
			}else {
				System.exit(0);
				break;
			}
		}
	}
}
