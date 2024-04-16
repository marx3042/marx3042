class UpDown :
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def printUpDown(self):
        winNum = 0
        if self.num1 > self.num2:
            winNum = "둘 중 더 큰 값은 {} 이다.".format(self.num1)
        elif self.num1 == self.num2:
            winNum = "두 수 모두 같다"
        else :
            winNum = "둘 중 더 큰 값은 {} 이다.".format(self.num2)
        
        return winNum


    

if __name__ == "__main__":
    inputNum1 = int(input("비교할 첫번 째 숫자를 입력하세요 : "))
    inputNum2 = int(input("비교할 두번 째 숫자를 입력하세요 : "))
    
    up_down = UpDown(inputNum1, inputNum2)
    print(up_down.printUpDown())
    
    
