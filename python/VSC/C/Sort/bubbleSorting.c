#include<stdio.h>
#include<stdlib.h>
#include<time.h>

int main(void) {
	int arData[30];
    int sort;
	srand(time(NULL));
	for (int i = 0; i < 30; i++) {
		arData[i] = (rand() % 999) + 1;
	}

	for (int i = 0; i < 30; i++) {
		printf("%d\t", arData[i]);
	}

printf("\n");
printf("\n");
    for(int i = 0 ; i<30;i++){
        for(int j = 0 ; j<30;j++){
            if(arData[j]<arData[j+1]){
                sort = arData[j+1];
                arData[j+1] = arData[j];
                arData[j] = sort;
            }
        }
    }

	for (int i = 0; i < 30; i++) {
		printf("%d\t", arData[i]);
	}

	return 0;
}