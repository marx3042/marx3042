#include<stdio.h>
#include<stdlib.h>
#include<time.h>

int main(void) {
	int arData[30];
	int pivot;
    int sort;

	srand(time(NULL));
	for (int i = 0; i < 30; i++) {
		arData[i] = (rand() % 999) + 1;
		printf("%d\t", arData[i]);
	}

	printf("\n");
	printf("\n");
	int num;
	int index;
	for (int i = 0; i < 30; i++) {
		pivot = 0;
		for(int j = i ;j<30;j++){
			if(pivot<arData[j]){
				pivot = arData[j];
				index = j;
			}
		}
		num = arData[i];
		arData[i] = pivot;
		arData[index] = num;
		
	}
	for (int i = 0; i < 30; i++) {
		printf("%d\t", arData[i]);
	}

	return 0;
}