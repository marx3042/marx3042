#include <stdio.h>
#include <stdbool.h>
#include "header.h"

int solution(int num, int n){
	if (num == n)	return false;
	if ((int)num % (int)n == 0){
		return true;
	}
	return false;
}
