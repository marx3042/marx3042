#include <stdio.h>

int main(){
    int num;
    char name = 'a';
    scanf("%d", &num);
    
    switch (num) {
    // num�� �޾ƿԴ�. num�� �����̹Ƿ� case ''�� ''�� ������ ���� ���̴�. 1, 2, 3�� �翬�� �ٲ� ��� ����.
    case 1:
        num = num * 2;
        printf("1���� �Է�\n");
        break;
    case 2:
        name = 'b';
        break;
    case 3:
        break;
    default:
        printf("1, 2, 3 �̿��� ���� ���� default�� ���Դ�!\n");
        break;
    }

    printf("%c\n", name);

    return 0;
}