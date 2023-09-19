#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "header.h"

int main(){
	srand(time(NULL));
	int random = 0;
	int random2 = 0;

	random = (rand() % 99) + 2;
	random2 = (rand() % 9) + 2;
	
	if(solution((int)random, (int)random2)){
		printf("1\n");
	}
	else{
		printf("0\n");
	}

	
	return 0;
}
