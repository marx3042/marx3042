from multiprocessing.resource_sharer import stop


inputNum = int(input())

for i in range(inputNum,0,-2):
    for j in range(inputNum, i, -2):
        print(" ", end = "")
    for j in range(i):
        print("*", end = "")
    print()
for i in range(3,inputNum+1,2):
    for j in range(inputNum-i,0,-2):
        print(" ", end = "")
    for j in range(i):
        print("*", end = "")
    print()
