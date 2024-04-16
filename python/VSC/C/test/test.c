#include <stdio.h>

float add(float a, int b){
    float sum = a + b;

    return sum;
}

int main(){
    //나이와 뺄 숫자
    int age = 27, num = 5;
    
    //출력 함수
    printf("저의 나이에서 %d을 뺀 값은 %d입니다. 저의 나이는 %d입니다.\n", num, (age - num), age);
    float sum = add(age, num);

    return 0;
}

// 메인 함수를 작성/선언 '함수'의 타입 함수명 (매개변수) {내용 입력과 리턴 값 설정}



