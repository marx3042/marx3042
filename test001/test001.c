#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "header.h"

int main(){
    srand(time(NULL));
    int num1 = rand() % 10001;
    int num2 = rand() % 10001;
    printf("%d %d : %d\n", num1, num2, solution(num1, num2));
    return 0;
}