package collectionTest;

import java.time.Duration;
import java.time.Instant;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.stream.IntStream;

public class SpeedTest {
	public static void main(String[] args) {
		final int SIZE = 10_000_000;
		final List<Integer> arrayList = new ArrayList<Integer>();
		final Set<Integer> hashSet = new HashSet<>();
		final int DATA = 8_888_888;
		
		//순차 병렬 집계 연산
		IntStream.range(0,  SIZE).forEach(value -> {
			arrayList.add(value);
			hashSet.add(value);
		});
		
		Instant start = Instant.now();
		arrayList.contains(DATA);
		Instant end = Instant.now();
		long elapsedTime = Duration.between(start, end).toMillis();
		System.out.println("arrayList 검색시간 : " + elapsedTime + "밀리초");
		
		start = Instant.now();
		hashSet.contains(DATA);
		end = Instant.now();
		elapsedTime = Duration.between(start, end).toMillis();
		System.out.println("arrayList 검색시간 : " + elapsedTime + "밀리초");
	}
}
