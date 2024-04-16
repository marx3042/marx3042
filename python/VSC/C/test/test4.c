#include <stdio.h>

int main(){
    int num = 0;

    while(1){
        printf("입력 대기 : ");
        scanf("%d", &num);

        if (num == 1){
            break;
        }
        
        printf("%d를 입력!!\n", num);

        if (num == 5){
            printf("5를 입력한 규리!!\n");
        }
    }
    
    return 0;
}