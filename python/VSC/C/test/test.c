#include <stdio.h>

float add(float a, int b){
    float sum = a + b;

    return sum;
}

int main(){
    //���̿� �� ����
    int age = 27, num = 5;
    
    //��� �Լ�
    printf("���� ���̿��� %d�� �� ���� %d�Դϴ�. ���� ���̴� %d�Դϴ�.\n", num, (age - num), age);
    float sum = add(age, num);

    return 0;
}

// ���� �Լ��� �ۼ�/���� '�Լ�'�� Ÿ�� �Լ��� (�Ű�����) {���� �Է°� ���� �� ����}



