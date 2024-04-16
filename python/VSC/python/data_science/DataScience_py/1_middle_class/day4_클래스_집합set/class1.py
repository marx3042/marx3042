### 함수
def transfASCII(flag, char, key):
    offset = ord(key) - ord('0')
    
    if flag == 0:
        return chr( ord(char) + offset )
    else:
        return chr( ord(char) - offset )
   
### 클래스
class EnDec:
    def __init__(self, flag, string, key):
        self.en_dec = flag
        self.in_str = string
        self.key = key

    def EncDec(self):
        out_str = "" # 초기화
        for i in range(len(self.in_str )):
            out_str += transfASCII(self.en_dec, self.in_str[i], self.key)

        return out_str

def main():
    string = input("문자열을 입력하세요: ")
    key = input("암복호 키 값을 입력하세요: ")[0]   # 첫 문자를 키로 취함

    print(string)
    print(key)
    
    en_dec0 = EnDec(0, string, key) # 암호화 객체 생성
    print(en_dec0.EncDec()) ; print("\n")

    en_dec1 = EnDec(1, en_dec0.EncDec(), key) # 복호화 객체 생성
    print(en_dec1.EncDec())
    
### 실행
if __name__ == "__main__":
    main()

