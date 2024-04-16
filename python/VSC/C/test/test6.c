#include <stdio.h>

int  main(){
    int arr[5][2] = {{1,2}, {3, 4}, {5,6}, {7, 8}, {9, 10}};

    for (int i = 0; i < 5; i++){ 
        for(int j = 0; j < 2; j++){
            printf("%d ", arr[i][j]);
            
            if(arr[i][j] == 5){
                printf("\n");
            }
        }
        
        printf("\n");
    }

    return 0;
}