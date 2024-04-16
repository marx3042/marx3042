#include <stdio.h>

int main(){
    int arr[10] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};

    if(arr[0] < arr[1] && arr[1] < arr[2]){
        printf("1번 조건 성립\n");
        if (arr[2] < arr[3] || arr[3] > arr[4]){
            printf("1번째 if안에 조건도 성립\n");
        }
    }
    else if((arr[arr[0]] == arr[0] && arr[0] > arr[1]) || arr[1] < arr[9]){
        printf("1번 조건이 성립하지 않을 때 2번 조건 성립\n");
    }
    else{
        printf("그 외의 조건 성립\n");
    }
    
    return 0;
}