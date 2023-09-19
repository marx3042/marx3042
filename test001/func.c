#include <stdio.h>
<<<<<<< HEAD
#include "header.h"

int solution(int num1, int num2){
    if (num1 == num2){
        return 1;
    }
    else{
        return -1;
    }
}
=======
#include <stdbool.h>
#include "header.h"

int solution(int num, int n){
	if (num == n)	return false;
	if ((int)num % (int)n == 0){
		return true;
	}
	return false;
}
>>>>>>> fb53898d8830fb2b0ade49a3d273c245c1c4e9ff
