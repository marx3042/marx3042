#include <stdio.h>

int main(){
    int arr[10] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};

    if(arr[0] < arr[1] && arr[1] < arr[2]){
        printf("1�� ���� ����\n");
        if (arr[2] < arr[3] || arr[3] > arr[4]){
            printf("1��° if�ȿ� ���ǵ� ����\n");
        }
    }
    else if((arr[arr[0]] == arr[0] && arr[0] > arr[1]) || arr[1] < arr[9]){
        printf("1�� ������ �������� ���� �� 2�� ���� ����\n");
    }
    else{
        printf("�� ���� ���� ����\n");
    }
    
    return 0;
}