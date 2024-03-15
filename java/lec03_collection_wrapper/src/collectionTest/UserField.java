package collectionTest;

import java.util.ArrayList;
import java.util.Collections;

public class UserField {
	
	ArrayList<User> users = new ArrayList<>();
	//�ߺ��˻�
	public User overlap(String id) {
		User temp = null;
		
		for(int i = 0; i < users.size(); i++) {
			if(users.get(i).getId().equals(id)) {
				temp = users.get(i);
			}
		}
		return temp;
	}
	//ȸ������
	public void newSign(User u) {
		u.setPassword(encrypt(u.getPassword()));
		users.add(u);
		
	}
	//�α���
	public boolean login(String id, String password) {
		User user = overlap(id);
		
		if(user != null) {
			if(user.getPassword().equals(encrypt(password))) {
				return true;
			}
		}
		return false;
	}
	//��ȣȭ
	public String encrypt(String pw) {
		String enPw = "";
		
		for(int i = 0; i < pw.length(); i++) {
			enPw += (char)(pw.charAt(i) * 3);
		}
		return enPw;
	}
	
	
	
}
