package maker;

import java.util.ArrayList;
import java.util.List;

public class TV {
	
	
	
	public static void checkAni(Video[] videos) {
		
		int count = 0;
		for(int i = 0; i < videos.length; i++) {
			if(videos[i] instanceof Ani) {
				count++;
			}
		}
		System.out.println(count);
	}
	
	public static void main(String[] args) {
		
		List<Video> vi = new ArrayList<Video>();
		
		vi.add(new DemonSlayer());
		
		for(Video v : vi) {
			
		}
		
		Video[] v = {
				new DemonSlayer(),
				new YourName(),
				new Titanic(),
				new Zzanggu(),
				};
		
		checkAni(v);
	}
}
