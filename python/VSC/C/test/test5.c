#include <stdio.h>

int main(){
    int a = 97;
    int num = 5;
    
    for(int i = 0; i < num; i++){
        printf("%c ", (char)(a + i));
    }
    
    printf("\n");

    for(int i = 0; i < num*2; i+=2){
        printf("%c ", (char)(a + i));
    }

    return 0;
}