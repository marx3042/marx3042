#include <stdio.h>

int main(){
    int num = 0;

    while(1){
        printf("�Է� ��� : ");
        scanf("%d", &num);

        if (num == 1){
            break;
        }
        
        printf("%d�� �Է�!!\n", num);

        if (num == 5){
            printf("5�� �Է��� �Ը�!!\n");
        }
    }
    
    return 0;
}