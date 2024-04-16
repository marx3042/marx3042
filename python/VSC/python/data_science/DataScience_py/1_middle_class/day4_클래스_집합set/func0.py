### 함수
def dumpASCII():
    for i in range(128):
        print(chr(i), end= ' ')

    print("\n")

    for i in range(128):
       print(ord(chr(i)), end= ' ')

    print("\n")
 
def main():
    dumpASCII()

### 실행
if __name__ == "__main__":
    main()

