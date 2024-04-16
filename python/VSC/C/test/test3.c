#include <stdio.h>

int main(){
    int num;
    char name = 'a';
    scanf("%d", &num);
    
    switch (num) {
    // num을 받아왔다. num은 정수이므로 case ''에 ''는 정수가 들어갔을 뿐이다. 1, 2, 3은 당연히 바뀌어도 상관 없다.
    case 1:
        num = num * 2;
        printf("1번을 입력\n");
        break;
    case 2:
        name = 'b';
        break;
    case 3:
        break;
    default:
        printf("1, 2, 3 이외의 수가 들어와 default에 들어왔다!\n");
        break;
    }

    printf("%c\n", name);

    return 0;
}