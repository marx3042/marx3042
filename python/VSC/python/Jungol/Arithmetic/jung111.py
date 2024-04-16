num1=int(input())
num2=int(input())
num3=int(input())
num4=int(input())
sum=num1+num2+num3+num4
avg=sum/4
print("sum",sum)
print("avg", "%.0f"%avg)

sum = 0

for i in range(4):
    inNum = int(input())
    sum += inNum

avg = sum / 4